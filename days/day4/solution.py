import sys
from pathlib import Path


def part_1(raw_input: str) -> float:
    grid, s = parse_input(raw_input), 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            c = grid[i][j]
            if c == ".":
                continue
            s += int(is_accessible(i, j, grid))
    return s


def part_2(raw_input: str) -> float:
    grid, s = parse_input(raw_input), 0

    def remove_accessible():
        accessible = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                c = grid[i][j]
                if c == ".":
                    continue
                if is_accessible(i, j, grid):
                    accessible.add((i, j))
        for i, j in accessible:
            row = list(grid[i])
            row[j] = "."
            grid[i] = "".join(row)
        return len(accessible)

    while True:
        d = remove_accessible()
        s += d
        if d == 0:
            break
    return s


def is_accessible(i, j, grid):
    n, m, s = len(grid), len(grid[0]), 0
    for dy, dx in [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]:
        s += int(0 <= i + dy < n and 0 <= j + dx < m and grid[i + dy][j + dx] == "@")
        if s >= 4:
            return False
    return True


def parse_input(raw_input: str) -> list[str]:
    return raw_input.splitlines()


input_filename = sys.argv[1]
part = sys.argv[2]
current_input = open(Path(__file__).parent.joinpath(input_filename)).read()
match part:
    case "1":
        print(part_1(current_input))
    case "2":
        print(part_2(current_input))
