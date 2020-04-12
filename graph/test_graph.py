#!/usr/bin/env python3

from bfs import bfs
from dfs import dfs
from dijkstra import DijkstraGraph
from kruskal_min_tree import KruskalTree
from prim_min_tree import PrimTree
from floyd_warshall import floyd_warshall


graph = {0: [(1, 4), (7, 8)],
         1: [(2, 8), (7, 11)],
         2: [(3, 7), (8, 2), (5, 4)],
         3: [(4, 9), (5, 14)],
         4: [(5, 10)],
         5: [(6, 2)],
         6: [(7, 1), (8, 6)],
         7: [(8, 7)]}

unweighted_graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4],
}

# source: [(dest, weight), (dest1, weight1)]
undirected_graph = {1: [(2, 5), (3, 3)],
                    2: [(3, 1)],
                    3: [(4, 5)],
                    4: [(1, 2), (2, 2)]}


directed_graph = {1: [(2, 3), (3, 4)],
                  2: [(3, 5)],
                  3: [(1, 10)],
                  4: [(1, 4), (3, 2), (2, 3)]}


def print_delimiter(func):
    def printing():
        func()
        print('_' * 50, end="\n\n")
    return printing


@print_delimiter
def test_bfs():
    start = 0
    print("BFS")
    print("Graph:", unweighted_graph)
    print(f"start is '{start}'")
    print(bfs(unweighted_graph, start))


@print_delimiter
def test_dfs():
    start = 0
    print("DFS")
    print("Graph:", unweighted_graph)
    print(f"start is '{start}'")
    print(dfs(unweighted_graph, start))


@print_delimiter
def test_dijkstra():
    print("Dijkstra")
    print("Graph:", graph)
    dijkstra = DijkstraGraph(graph, is_undirected=True)
    source = 0
    destination = 4
    print(f"source is {source}, destination is {destination}")
    dijkstra.explore(source)
    path = dijkstra.get_path(source, destination)
    print(path, f"is the shortest path from {source} to {destination}")
    cost = dijkstra.get_cost(source, destination)
    print(cost, f"is cost of the path from {source} to {destination}")


@print_delimiter
def test_kruskal():
    print("Kruskal")
    print("graph:", undirected_graph)
    tree = KruskalTree(undirected_graph).explore_tree()
    print("minimal spanning tree:", tree)


@print_delimiter
def test_prim():
    start = 0
    print("Prim's alg")
    print("graph:", undirected_graph)
    print(f"start is {start}")

    prim = PrimTree(undirected_graph)

    tree = prim.prim(start)
    print("minimal spanning tree:", tree)

    prim = PrimTree(undirected_graph)
    tree = prim.prim_heap(start)
    print("Using min heap:")
    print("minimal spanning tree:", tree)


@print_delimiter
def test_floyd_warshall():
    print("Floyd-Warshall alg")
    print("Graph:", directed_graph)
    print("Table with distances:")
    dist_table = floyd_warshall(directed_graph)
    for row in dist_table:
        for val in row:
            print ('{:5}'.format(val), end="")
        print()


if __name__ == "__main__":
    test_bfs()
    test_dfs()
    test_dijkstra()
    test_kruskal()
    test_prim()
    test_floyd_warshall()
