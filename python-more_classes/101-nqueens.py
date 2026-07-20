                                                                                                                                                        i#!/usr/bin/env python3
import sys
from itertools import permutations


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("error: N must be a number", file=sys.stderr)
        sys.exit(1)

    if n < 4:
        print("error: N must be at least 4", file=sys.stderr)
        sys.exit(1)

    cols = range(n)
    for perm in permutations(cols):
        diagonals_ok = n == len(set(perm[i] + i for i in cols)) == len(set(perm[i] - i for i in cols))
        if diagonals_ok:
            print(list(perm))


if __name__ == "__main__":
    main()
