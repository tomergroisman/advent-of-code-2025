import sys
from pathlib import Path


def part_1(raw_input: str) -> float:
    banks = parse_input(raw_input)
    joltage_sum = 0
    for bank in banks:
        joltage_sum += get_max_joltage(bank, 2)
    return joltage_sum


def part_2(raw_input: str) -> float:
    banks = parse_input(raw_input)
    joltage_sum = 0
    for bank in banks:
        joltage_sum += get_max_joltage(bank, 12)
    return joltage_sum


def get_max_joltage(bank: str, n: int) -> float:
    digits = []
    for j in range(1, n + 1):
        safe_offset = n - j
        d = max(bank[:-safe_offset] if safe_offset > 0 else bank)
        digits.append(d)
        i = bank.index(d)
        bank = bank[i + 1 :]
    return int("".join(digits))


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
