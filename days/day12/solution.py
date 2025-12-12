import sys
from pathlib import Path

import numpy as np
import shapely
from matplotlib import pyplot as plt
from shapely.plotting import plot_polygon


def part_1(raw_input: str) -> float:
    trees, ans = parse_input(raw_input), 0
    for tree in trees:
        key, polygons = tree
        max_area = np.prod([int(n) for n in key.split("x")])
        area_sum = sum([p.area for p in polygons])
        if max_area >= area_sum:
            ans += 1
    return ans


def part_2(raw_input: str) -> float:
    parse_input(raw_input)
    return 0


def parse_input(raw_input: str):
    sections = raw_input.split("\n\n")
    presents = []
    for raw in sections[:-1]:
        (
            parts,
            cells,
        ) = (
            raw.split("\n")[1:],
            [],
        )
        h = len(parts)
        for i in range(len(parts)):
            for j in range(len(parts[0])):
                if parts[i][j] == "#":
                    cells.append(shapely.box(j, h - i, j + 1, h - i - 1))
        polygon = shapely.union_all(cells)
        presents.append(polygon)
    trees = []
    for it in sections[-1].splitlines():
        key, present_ids_str = it.split(": ")
        present_count = [int(n) for n in present_ids_str.split(" ")]
        trees.append((key, []))
        for i, count in enumerate(present_count):
            for _ in range(count):
                trees[-1][1].append(presents[i])
    return trees


def plot(polygon):
    plot_polygon(polygon)
    plt.gca().set_aspect("equal")
    plt.grid(True)
    plt.show()


input_filename = sys.argv[1]
part = sys.argv[2]
current_input = open(Path(__file__).parent.joinpath(input_filename)).read()
match part:
    case "1":
        print(part_1(current_input))
    case "2":
        print(part_2(current_input))
