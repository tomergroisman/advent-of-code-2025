import sys
from pathlib import Path
from functools import lru_cache

import numpy as np


def part_1(raw_input: str) -> float:
    def bfs(s):
        q, sp, v = [s], set(), set()
        while q:
            p = q.pop(0)
            if p in v or p[0] == len(g):
                continue
            v.add(p)
            if g[p[0]][p[1]] == "^":
                sp.add(p)
                q.append((p[0], p[1] - 1))
                q.append((p[0], p[1] + 1))
            else:
                q.append((p[0] + 1, p[1]))
        return len(sp)

    g = np.array(parse_input(raw_input))
    m, s = len(g[0]), None
    for j in range(m):
        if g[0][j] == "S":
            s = (0, j)
    return bfs(s)


def part_2(raw_input: str) -> float:
    @lru_cache(maxsize=None)
    def dfs(p):
        if p[0] == len(g):
            return 1
        if g[p[0]][p[1]] == "^":
            return dfs((p[0], p[1] - 1)) + dfs((p[0], p[1] + 1))
        return dfs((p[0] + 1, p[1]))

    g = np.array(parse_input(raw_input))
    m, s = len(g[0]), None
    for j in range(m):
        if g[0][j] == "S":
            s = (0, j)
    return dfs(s)


def parse_input(raw_input: str) -> list[list[str]]:
    return [list(row) for row in raw_input.splitlines()]


input_filename = sys.argv[1]
part = sys.argv[2]
current_input = open(Path(__file__).parent.joinpath(input_filename)).read()
match part:
    case "1":
        print(part_1(current_input))
    case "2":
        print(part_2(current_input))
