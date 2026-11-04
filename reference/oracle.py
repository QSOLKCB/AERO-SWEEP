"""Independent AS-001 det2 oracle: Python arbitrary-precision integer arithmetic.

This is a mathematical reference, not a port of the Ada implementation.
Rows are (a, b), (c, d); determinant equals a*d - b*c.
"""
from __future__ import annotations

import json
import sys

LIMIT = 32767


def compute_exact_determinant(a: int, b: int, c: int, d: int) -> dict[str, int | str]:
    values = (a, b, c, d)
    if any(type(value) is not int for value in values):
        raise TypeError("matrix elements must be Python integers, not booleans")
    if any(value < -LIMIT or value > LIMIT for value in values):
        return {"status": "INVALID_INPUT", "result": 0}
    return {"status": "OK", "result": a * d - b * c}


def main(args: list[str]) -> int:
    if len(args) != 4:
        print(json.dumps({"status": "PARSE_ERROR", "result": 0}, sort_keys=True))
        return 2
    try:
        values = [int(field, 10) for field in args]
    except ValueError:
        print(json.dumps({"status": "PARSE_ERROR", "result": 0}, sort_keys=True))
        return 2
    print(json.dumps(compute_exact_determinant(*values), sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
