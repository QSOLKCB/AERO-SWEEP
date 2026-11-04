"""Oracle tests do not depend on GNAT or invoke the Ada implementation."""
from __future__ import annotations

import json
from pathlib import Path
import unittest

from reference.oracle import compute_exact_determinant, main

FIXTURES = json.loads(
    (Path(__file__).parent / "fixtures" / "det2_cases.json").read_text(encoding="utf-8")
)


class OracleTests(unittest.TestCase):
    def test_pinned_cases(self) -> None:
        for case in FIXTURES:
            with self.subTest(case=case["id"]):
                expected = {"status": case["status"], "result": case["result"]}
                self.assertEqual(compute_exact_determinant(*case["values"]), expected)

    def test_detects_known_wrong_mapping(self) -> None:
        a, b, c, d = (1, 2, 3, 4)
        expected = compute_exact_determinant(a, b, c, d)
        mutant = a * b - c * d
        self.assertEqual(expected["result"], -2)
        self.assertNotEqual(expected["result"], mutant)

    def test_alternation_and_sign_flip(self) -> None:
        for a in range(-3, 4):
            for b in range(-3, 4):
                for c in range(-3, 4):
                    for d in range(-3, 4):
                        val = compute_exact_determinant(a, b, c, d)["result"]
                        swapped = compute_exact_determinant(b, a, d, c)["result"]
                        self.assertEqual(swapped, -val)
                        self.assertEqual(compute_exact_determinant(a, b, a, b)["result"], 0)

    def test_type_guard(self) -> None:
        with self.assertRaises(TypeError):
            compute_exact_determinant(True, 1, 2, 3)
        with self.assertRaises(TypeError):
            compute_exact_determinant(1.0, 1, 2, 3)


if __name__ == "__main__":
    unittest.main()
