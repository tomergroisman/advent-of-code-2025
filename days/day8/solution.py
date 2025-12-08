import sys
from itertools import combinations
from pathlib import Path

import numpy as np
import networkx as nx


def part_1(raw_input: str) -> float:
    g = get_graph(raw_input)
    con, t = nx.Graph(), 1000
    con.add_nodes_from(g.nodes)
    sorted_edges = sorted(g.edges(data=True), key=lambda x: x[2]["weight"])
    for i in range(t):
        min_e = sorted_edges.pop(0)
        u, v = min_e[0], min_e[1]
        con.add_edge(u, v)
    return np.prod(sorted([len(cir) for cir in nx.connected_components(con)])[-3:])


def part_2(raw_input: str) -> float:
    g = get_graph(raw_input)
    con = nx.Graph()
    con.add_nodes_from(g.nodes)
    sorted_edges, min_e = sorted(g.edges(data=True), key=lambda x: x[2]["weight"]), None
    while nx.number_connected_components(con) > 1:
        min_e = sorted_edges.pop(0)
        u, v = min_e[0], min_e[1]
        con.add_edge(u, v)
    return min_e[0][0] * min_e[1][0]


def get_d(a: tuple[int], b: tuple[int]) -> float:
    aa, ab = np.array(a), np.array(b)
    return np.sqrt(np.sum((aa - ab) ** 2))


def get_graph(raw_input: str) -> nx.Graph:
    parsed_input = parse_input(raw_input)
    g = nx.Graph()
    g.add_nodes_from(parsed_input)
    for u, v in combinations(g.nodes, 2):
        g.add_edge(u, v, weight=get_d(u, v))
    return g


def parse_input(raw_input: str) -> list[tuple[int, int, int]]:
    return [
        (int(it[0]), int(it[1]), int(it[2]))
        for it in [row.split(",") for row in raw_input.splitlines()]
    ]


input_filename = sys.argv[1]
part = sys.argv[2]
current_input = open(Path(__file__).parent.joinpath(input_filename)).read()
match part:
    case "1":
        print(part_1(current_input))
    case "2":
        print(part_2(current_input))
