import sys
from functools import lru_cache
from pathlib import Path
import matplotlib.pyplot as plt
import networkx as nx


def part_1(raw_input: str) -> float:
    G = parse_input(raw_input, False)
    return len(list(nx.all_simple_paths(G, source="you", target="out")))


def part_2(raw_input: str) -> float:
    @lru_cache(maxsize=None)
    def dfs(v, t):
        if v == t:
            return 1
        s = 0
        for u in G.successors(v):
            s += dfs(u, t)
        return s

    G = parse_input(raw_input, False)
    n1, n2 = "fft", "dac"
    p1 = dfs("svr", n1)
    p2 = dfs(n1, n2)
    p3 = dfs(n2, "out")
    return p1 * p2 * p3


def plot(G: nx.DiGraph, reds: set, blues: set):
    pos = nx.kamada_kawai_layout(G)
    colors = [
        "red" if n in reds else "blue" if n in blues else "lightblue" for n in G.nodes()
    ]
    sizes = [200 if n in reds or n in blues else 20 for n in G.nodes()]
    plt.figure(figsize=(8, 8))
    nx.draw(G, pos, node_color=colors, node_size=sizes, arrowsize=10, arrows=True)
    nx.draw_networkx_labels(G, pos)
    plt.show()


def parse_input(raw_input: str, part_2: bool) -> nx.DiGraph:
    conf = raw_input.splitlines()
    G = nx.DiGraph()
    for l in conf:
        v, le_temp = l.split(": ")
        E = le_temp.split(" ")
        if part_2:
            ambassador = next(
                (i for i, v in enumerate(E) if v == "dac" or v == "fft"), 0
            )
            G.add_edge(v, E[ambassador], weight=len(E))
        else:
            for e in E:
                G.add_edge(v, e)
    return G


input_filename = sys.argv[1]
part = sys.argv[2]
current_input = open(Path(__file__).parent.joinpath(input_filename)).read()
match part:
    case "1":
        print(part_1(current_input))
    case "2":
        print(part_2(current_input))
