"""Run the real Ada CLI against an independently derived Python oracle.

REQUIRES a compiled build/bin/det2_cli executable; never silently skip
when missing. Tests spawn the executable once per case (small fixed domain).
"""
from __future__ import annotations

import itertools
import json
import os
from pathlib import Path
import random
import subprocess
import unittest

from reference.oracle import compute_exact_determinant

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = json.loads(
    (ROOT / "tests" / "fixtures" / "det2_cases.json").read_text(encoding="utf-8")
)


class DifferentialTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.executable = Path(
            os.environ.get("AEROSWEEP_CLI", str(ROOT / "build" / "bin" / "det2_cli"))
        )
        if not cls.executable.is_file():
            raise RuntimeError(
                f"Ada CLI not built: {cls.executable}; run 'make build' first"
            )

    def compare_case(self, values: tuple[int, int, int, int] | list[int]) -> None:
        expected = compute_exact_determinant(*values)
        completed = subprocess.run(
            [str(self.executable), *(str(value) for value in values)],
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(completed.stderr, "")
        pieces = completed.stdout.split()
        self.assertEqual(len(pieces), 2, repr(completed.stdout))
        actual = {"status": pieces[0], "result": int(pieces[1])}
        self.assertEqual(actual, expected, f"inputs={values}")

    def test_cli_output_format(self) -> None:
        # A negative Ada 'Image has no leading space.  Exact protocol
        # formatting must not depend on sign or padding in 'Image.
        cases = (
            ((1, 2, 3, 4), "OK -2\n"),
            ((1, 0, 0, 1), "OK 1\n"),
            ((0, 0, 0, 0), "OK 0\n"),
            ((32768, 0, 0, 1), "INVALID_INPUT 0\n"),
        )
        for values, expected_output in cases:
            with self.subTest(values=values):
                completed = subprocess.run(
                    [str(self.executable), *(str(value) for value in values)],
                    check=False,
                    capture_output=True,
                    text=True,
                    timeout=10,
                )
                self.assertEqual(completed.returncode, 0, completed.stderr)
                self.assertEqual(completed.stderr, "")
                self.assertEqual(completed.stdout, expected_output)

    def test_pinned_cases(self) -> None:
        for case in FIXTURES:
            with self.subTest(case=case["id"]):
                self.compare_case(case["values"])

    def test_exhaustive_small_domain(self) -> None:
        domain = (-2, -1, 0, 1, 2)
        for values in itertools.product(domain, repeat=4):
            self.compare_case(values)

    def test_seeded_boundary_adversarial(self) -> None:
        rng = random.Random(20261105)
        domain = (-2147483648, -32768, -32767, -1, 0, 1, 32767, 32768, 2147483647)
        for _ in range(512):
            values = tuple(rng.choice(domain) for _ in range(4))
            self.compare_case(values)


if __name__ == "__main__":
    unittest.main()
