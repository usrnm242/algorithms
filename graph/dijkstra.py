#!/usr/bin/env python3

import math
import sys
from graph import Graph
import heapq


def decrease_key(queue, tup, new_distance):
    index = 0

    while index < len(queue) and queue[index] != tup:
        index = (2 * index + 2) if queue[index] < tup else (2 * index + 1)

    queue[index] = (new_distance, tup[1])

    return index


class DijkstraGraph(Graph):
    def __init__(self, graph, is_undirected=False):
        """
        init arg is matrix-like or dict-like graph
        first always call explore
        then show_distances or get_path
        """

        super(DijkstraGraph, self).__init__(graph, is_undirected)

        self.distance = [0 for _ in range(len(self))]
        self.path = [-1 for _ in range(len(self))]

    def explore(self, source):

        self.distance[source] = 0

        queue = []
        heapq.heappush(queue, (0, source))

        for u in self.graph.keys():
            if u != source:
                self.distance[u] = float("inf")
                self.path[u] = -1

        while queue:
            u = heapq.heappop(queue)[1]  # get dist here
            for v, weight in self.graph[u]:
                new_dist = self.distance[u] + weight
                if self.distance[v] > new_dist:
                    if self.distance[v] == float("inf"):
                        heapq.heappush(queue, (new_dist, v))
                    else:
                        index = decrease_key(queue,
                                             (self.distance[v], v),
                                             new_dist)
                        heapq._siftup(queue, index)
                    self.distance[v] = new_dist
                    self.path[v] = u

    def show_distances(self, source):
        print(f"Distance from node: {source}")
        for u in range(len(self)):
            print(f"Node {u} has distance: {self.distance[u]}")

    def show_path(self, source, dest):
        """
        call only after calling DijkstraGraph
        """

        path = []
        cost = 0
        tmp = dest
        # going from dest to source
        while self.path[tmp] != -1:
            path.append(tmp)
            if tmp != source:
                for v, weight in self.graph[tmp]:
                    if v == self.path[tmp]:
                        cost += weight
                        break
            tmp = self.path[tmp]
        path.append(source)
        path.reverse()

        print(f"Path to reach {dest} from {source}:")

        for u in path:
            print(f"{u}", end=" ")
            if u != dest:
                print("-> ", end="")

        print("\nTotal cost of path: ", cost)

    def get_path(self, source, dest) -> list:
        path = []
        cost = 0
        tmp = dest
        # going from dest to source
        while self.path[tmp] != -1:
            path.append(tmp)
            if tmp != source:
                for v, weight in self.graph[tmp]:
                    if v == self.path[tmp]:
                        cost += weight
                        break
            tmp = self.path[tmp]
        path.append(source)
        path.reverse()

        return path

    def get_cost(self, source, dest) -> int:
        cost = 0
        tmp = dest

        while self.path[tmp] != -1:
            if tmp != source:
                for v, weight in self.graph[tmp]:
                    if v == self.path[tmp]:
                        cost += weight
                        break
            tmp = self.path[tmp]

        return cost


if __name__ == "__main__":

    g = {0: [(1, 4), (7, 8)],
         1: [(2, 8), (7, 11)],
         2: [(3, 7), (8, 2), (5, 4)],
         3: [(4, 9), (5, 14)],
         4: [(5, 10)],
         5: [(6, 2)],
         6: [(7, 1), (8, 6)],
         7: [(8, 7)]}

    graph = DijkstraGraph(g, is_undirected=True)

    print(graph)
    source = 0
    destination = 4
    graph.explore(source)
    graph.show_distances(source)
    graph.show_path(source, destination)
    path = graph.get_path(source, destination)

    print('_' * 40, '\n')
    print("shortest path is", path)
