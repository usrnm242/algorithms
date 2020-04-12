#!/usr/bin/env python3

from copy import deepcopy

def floyd_warshall(graph: dict) -> 'list of lists':
    vertices = len(graph)

    g = [[float("inf") if i != j else 0.0
          for i in range(vertices)]
          for j in range(vertices)]

    for source in graph:
        for dest, weight in graph[source]:
            g[source - 1][dest - 1] = weight

    graph = g

    dist = deepcopy(graph)

    # check vertex k against all other vertices (i, j)
    for k in range(vertices):
        # looping through rows
        for i in range(vertices):
            # looping through columns
            for j in range(vertices):
                if (dist[i][k] != float("inf") \
                        and dist[k][j] != float("inf") \
                        and dist[i][k] + dist[k][j] < dist[i][j]):

                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


if __name__ == "__main__":

    graph = {1: [(2, 3), (3, 4)],
             2: [(3, 5)],
             3: [(1, 10)]}

    table = floyd_warshall(graph)

    for line in table:
        print(line)
