import sys
from pathlib import Path


def part_1(raw_input: str) -> float:
    rotations = parse_input(raw_input)
    dial, password = 50, 0
    for rotation in rotations:
        direction, distance = rotation[0], int(rotation[1:])
        if direction == "L":
            dial = (dial - distance) % 100
        if direction == "R":
            dial = (dial + distance) % 100

        if dial == 0:
            password += 1
    return password


def part_2(raw_input: str) -> float:
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    rotations = parse_input(raw_input)
    dial, password = 50, 0
    for rotation in rotations:
        direction, distance = rotation[0], int(rotation[1:])
        op = subtract if direction == "L" else add
        for i in range(distance):
            dial = op(dial, 1) % 100
            if dial == 0:
                password += 1
    return password


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
