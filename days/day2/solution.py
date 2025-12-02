import sys
from pathlib import Path


def part_1(raw_input: str) -> float:
    ranges = parse_input(raw_input)
    invalid_ids = []
    for start, end in ranges:
        for id in range(start, end + 1):
            if validate_id(id, False):
                invalid_ids.append(id)
    return sum(invalid_ids)


def part_2(raw_input: str) -> float:
    ranges = parse_input(raw_input)
    invalid_ids = []
    for start, end in ranges:
        for id in range(start, end + 1):
            if validate_id(id, True):
                invalid_ids.append(id)
    return sum(invalid_ids)


def parse_input(raw_input: str) -> list[tuple[int, int]]:
    return [
        (int(n[0]), int(n[1]))
        for n in (tuple(r.split("-")) for r in raw_input.split(","))
    ]


def validate_id(id: int, part_2: bool):
    id_str = str(id)
    n = len(id_str)

    if not part_2:
        if (n % 2) != 0:
            return False
        return id_str[: (n // 2)] == id_str[(n // 2) :]

    for i in range(n):
        pattern = id_str[:i]
        pattern_count = id_str.count(pattern)
        if pattern_count * i == n:
            return True
    return False


input_filename = sys.argv[1]
part = sys.argv[2]
current_input = open(Path(__file__).parent.joinpath(input_filename)).read()
match part:
    case "1":
        print(part_1(current_input))
    case "2":
        print(part_2(current_input))
