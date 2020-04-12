#!/usr/bin/env python3

import heapq as hq
from numpy import Infinity


class Vertex:
    def __init__(self, id):
        self.id = str(id)
        self.key = None
        self.pi = None
        self.neighbors = []
        self.edges = {}  # {vertex: distance}

    def __lt__(self, other):
        return self.key < other.key

    def __repr__(self):
        return self.id

    def add_neighbor(self, vertex):
        self.neighbors.append(vertex)

    def add_edge(self, vertex, weight):
        self.edges[vertex.id] = weight


class Graph:
    def __init__(self, input_graph: dict):
        self.graph = [Vertex(source) for source in input_graph]

        for source in input_graph:
            for dest, weight in input_graph[source]:
                self._connect(source, dest, weight)

    def _connect(self, a, b, edge):
        # add the neighbors:
        self.graph[a - 1].add_neighbor(self.graph[b - 1])
        self.graph[b - 1].add_neighbor(self.graph[a - 1])
        # add the edges:
        self.graph[a - 1].add_edge(self.graph[b - 1], edge)
        self.graph[b - 1].add_edge(self.graph[a - 1], edge)


class PrimTree(Graph):
    def __init__(self, input_graph: dict):
        super(PrimTree, self).__init__(input_graph)
        self.source = None

    def prim(self, source) -> list:
        """Prim's Algorithm.

            Runtime:
                O(mn) with m edges and n vertices

            Usage:
                PrimTree(graph).prim(0)
        """

        # self._connect(source, source, 0)

        self.source = self.graph[source]

        for u in self.graph:
            u.key = Infinity
            u.pi = None
        self.source.key = 0
        q = self.graph[:]
        while q:
            u = min(q)
            q.remove(u)
            for v in u.neighbors:
                if (v in q) and (u.edges[v.id] < v.key):
                    v.pi = u
                    v.key = u.edges[v.id]

        tree = []

        for i in range(1, len(self.graph)):
            tree.append((int(self.graph[i].id), int(self.graph[i].pi.id)))

        return tree

    def prim_heap(self, source):
        """Prim's Algorithm with min heap.

            Runtime:
                O((m + n)log n) with m edges and n vertices

            Usage:
                PrimTree(graph).prim(0)
        """

        # self._connect(source, source, 0)
        self.source = self.graph[source]

        for u in self.graph:
            u.key = Infinity
            u.pi = None
        self.source.key = 0

        h = [v for v in self.graph]
        hq.heapify(h)

        while h:
            u = hq.heappop(h)
            for v in u.neighbors:
                if (v in h) and (u.edges[v.id] < v.key):
                    v.pi = u
                    v.key = u.edges[v.id]
                    hq.heapify(h)

        tree = []

        for i in range(1, len(self.graph)):
            # + 1
            tree.append((int(self.graph[i].id), int(self.graph[i].pi.id)))

        return tree


if __name__ == "__main__":

    undirected_graph = {1: [(2, 5), (3, 3)],
                        2: [(3, 1)],
                        3: [(4, 5)],
                        4: [(1, 2), (2, 2)]}

    t = PrimTree(undirected_graph)

    a = t.prim(0)
    print(a)

    print('_' * 40, end='\n\n')

    t = PrimTree(undirected_graph)

    b = t.prim_heap(0)
    print(b)
