import sys
from pathlib import Path
import re
import numpy as np
from scipy.optimize import linprog


def part_1(raw_input: str) -> float:
    def bfs(machine):
        final, buttons, _ = machine
        q, vt = [("." * len(final), 0)], set()
        while True:
            current, t = q.pop(0)
            if current == final:
                return t
            if current in vt:
                continue
            vt.add(current)
            for button in buttons:
                new_temp = list(current)
                for indicator in button:
                    new_temp[indicator] = "." if new_temp[indicator] == "#" else "#"
                new = "".join(new_temp)
                q.append((new, t + 1))

    machines, s = parse_input(raw_input), 0
    for i in range(len(machines)):
        s += bfs(machines[i])
    return s


def part_2(raw_input: str) -> float:
    machines, s = parse_input(raw_input), 0
    for machine in machines:
        _, buttons, joltage = machine
        build_M = [[0] * len(buttons) for _ in range(len(joltage))]
        for i in range(len(buttons)):
            button = buttons[i]
            for j in button:
                build_M[j][i] += 1
        c = [1 for _ in buttons]
        M = np.array(build_M)
        b = np.array(list(joltage))
        a = linprog(c, A_eq=M, b_eq=b, integrality=1).fun
        s += a
    return int(s)


def parse_input(raw_input: str):
    rows = raw_input.splitlines()
    res = []
    for row in rows:
        state, buttons, joltage = re.split(r"\[(.*)] (\(.*\)) (\{.*})", row)[1:-1]
        buttons = [
            list(map(int, sub))
            for sub in [str_t.strip("()").split(",") for str_t in buttons.split(" ")]
        ]
        joltage = [int(n) for n in joltage.strip("{}").split(",")]
        res.append((state, buttons, joltage))
    return res


input_filename = sys.argv[1]
part = sys.argv[2]
current_input = open(Path(__file__).parent.joinpath(input_filename)).read()
match part:
    case "1":
        print(part_1(current_input))
    case "2":
        print(part_2(current_input))
