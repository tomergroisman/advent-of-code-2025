import sys
from itertools import combinations
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as patches


def part_1(raw_input: str) -> float:
    ps, areas = parse_input(raw_input), []
    for p1, p2 in combinations(ps, 2):
        areas.append(calc_area(p1, p2))
    return max(areas)


def part_2(raw_input: str) -> float:
    ps, areas = parse_input(raw_input), []
    for p1, p2 in combinations(ps, 2):
        areas.append((calc_area(p1, p2), p1, p2))
    sorted_area = sorted(areas, reverse=True, key=lambda x: x[0])
    sides = [(ps[-1], ps[0])]
    for i in range(len(ps) - 1):
        sides.append((ps[i], ps[i + 1]))
    for area in sorted_area:
        if not is_intersects_with_side(area[1], area[2], sides, area[0] == 2388372940):
            plot(ps, area[1], area[2])
            return area[0]
    return 0


def is_intersects_with_side(p1, p2, sides, log):
    (x1, y1), (x2, y2) = p1, p2
    for side in sides:
        (sx1, sy1), (sx2, sy2) = side
        is_x_in_range = (sx1 > x1 or sx1 > x2 or sx2 > x1 or sx2 > x2) and (
            sx1 < x1 or sx1 < x2 or sx2 < x1 or sx2 < x2
        )
        is_y_in_range = (sy1 > y1 or sy1 > y2 or sy2 > y1 or sy2 > y2) and (
            sy1 < y1 or sy1 < y2 or sy2 < y1 or sy2 < y2
        )
        if is_x_in_range and is_y_in_range:
            return True
    return False


def calc_area(p1, p2):
    d1 = abs(p1[0] - p2[0]) + 1
    d2 = abs(p1[1] - p2[1]) + 1
    return d1 * d2


def parse_input(raw_input: str) -> list[tuple[int, int]]:
    return [
        (int(p[0]), int(p[1]))
        for p in [row.split(",") for row in raw_input.splitlines()]
    ]


def plot(ps, p1, p2):
    fig, ax = plt.subplots()
    poly = patches.Polygon(
        ps,
        closed=True,
        facecolor="green",
        alpha=0.5,  # area 50% opacity
        edgecolor="green",
        linewidth=2,
    )
    ax.add_patch(poly)

    xs, ys = zip(*ps)
    ax.plot(xs, ys, "ro", markersize=1)  # "ro" = red circle markers

    ax.set_xlim(min(xs) - 1, max(xs) + 1)
    ax.set_ylim(min(ys) - 1, max(ys) + 1)
    ax.set_aspect("equal")
    plt.grid(True)

    x_low, x_high = sorted([p1[0], p2[0]])
    y_low, y_high = sorted([p1[1], p2[1]])
    width = x_high - x_low
    height = y_high - y_low
    rect = patches.Rectangle(
        (x_low, y_low),
        width,
        height,
        linewidth=1,
        edgecolor="blue",
        facecolor="none",
        zorder=10,
    )
    plt.gca().add_patch(rect)

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
