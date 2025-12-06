import sys
from pathlib import Path
import numpy as np


def part_1(raw_input: str) -> float:
    g = parse_input(raw_input, False)
    n, m, solutions = len(g), len(g[0]), []
    for j in range(m):
        op = np.sum if g[-1][j] == "+" else np.prod
        col = [int(str_n) for str_n in g[:-1, j]]
        solutions.append(op(col))
    return sum(solutions)


def part_2(raw_input: str) -> float:
    def normalize_col(col):
        n, m, new_col = len(col), len(col[0]), []
        for j in range(m - 1, -1, -1):
            new_col.append("")
            for i in range(n):
                if col[i][j] == " ":
                    continue
                new_col[-1] = new_col[-1] + col[i][j]
            new_col[-1] = int(new_col[-1])
        return new_col

    g = parse_input(raw_input, True)
    n, m, solutions = len(g), len(g[0]), []
    for j in range(m - 1, -1, -1):
        op = np.sum if g[-1][j].strip() == "+" else np.prod
        solutions.append(op(normalize_col(g[:-1, j])))
    return sum(solutions)


def parse_input(raw_input: str, part_2: bool):
    if not part_2:
        return np.array(
            [
                row.split(" ")
                for row in [" ".join(row.split()) for row in raw_input.splitlines()]
            ]
        )

    raw_g = raw_input.splitlines()
    for j, c in enumerate(raw_g[-1]):
        if j == 0:
            continue
        if c != " ":
            for i in range(len(raw_g)):
                raw_row = list(raw_g[i])
                raw_row[j - 1] = "#"
                raw_g[i] = "".join(raw_row)
    return np.array([row.split("#") for row in raw_g])


input_filename = sys.argv[1]
part = sys.argv[2]
current_input = open(Path(__file__).parent.joinpath(input_filename)).read()
match part:
    case "1":
        print(part_1(current_input))
    case "2":
        print(part_2(current_input))
