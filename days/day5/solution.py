import sys
from pathlib import Path


def part_1(raw_input: str) -> float:
    ranges, ids = parse_input(raw_input)

    def is_fresh(id: str, ranges: list[str]) -> bool:
        for range in ranges:
            s, e = range.split("-")
            if int(s) <= int(id) <= int(e):
                return True
        return False

    return sum([is_fresh(id, ranges) for id in ids])


def part_2(raw_input: str) -> float:
    ranges, _ = parse_input(raw_input)
    nr = [[int(r[0]), int(r[1])] for r in [r.split("-") for r in ranges]]
    nr.sort()

    mr = [nr[0]]
    for s, e in nr[1:]:
        if s <= mr[-1][1]:
            mr[-1][1] = max(e, mr[-1][1])
        else:
            mr.append([s, e])

    return sum([r[1] - r[0] + 1 for r in mr])


def parse_input(raw_input: str) -> tuple[list[str], list[str]]:
    return tuple([part.splitlines() for part in raw_input.split("\n\n")])


input_filename = sys.argv[1]
part = sys.argv[2]
current_input = open(Path(__file__).parent.joinpath(input_filename)).read()
match part:
    case "1":
        print(part_1(current_input))
    case "2":
        print(part_2(current_input))
