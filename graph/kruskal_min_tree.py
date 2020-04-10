from graph import Graph


class KruskalTree(Graph):
    def __init__(self, graph):
        """
        init arg is matrix-like or dict-like graph
        first always call explore
        then show_distances or get_path
        """

        super(KruskalTree, self).__init__(graph, is_undirected=True)
        self.vertexes = graph.keys()
        self.edges = self.__get_sorted_edges()

    def __get_sorted_edges(self):
        res = []

        source_dest_set = []

        for source in self.graph:
            for destination, weight in self.graph[source]:
                source_dest_set.append((source, destination))
                if (source, destination) not in source_dest_set \
                        or (destination, source) not in source_dest_set:
                    res.append((weight, source, destination))

        return sorted(res, key=lambda edge: edge[0])

    def explore_tree(self):
        parent = dict()
        rank = dict()

        def make_set(vertex):
            parent[vertex] = vertex
            rank[vertex] = 0

        def find(vertex):
            if parent[vertex] != vertex:
                parent[vertex] = find(parent[vertex])
            return parent[vertex]

        def union(vertex1, vertex2):
            root1 = find(vertex1)
            root2 = find(vertex2)

            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                else:
                    parent[root1] = root2
                    if rank[root1] == rank[root2]:
                        rank[root2] += 1

        for vertex in self.vertexes:
            make_set(vertex)

        minimum_spanning_tree = set()

        for edge in self.edges:
            weight, vertex1, vertex2 = edge
            print(weight, vertex1, vertex2)
            if find(vertex1) != find(vertex2):
                union(vertex1, vertex2)
                minimum_spanning_tree.add(edge)

        return minimum_spanning_tree


if __name__ == '__main__':

    weight = 1

    g = {1: [(2, 5), (3, 3)],
         2: [(3, 1)],
         3: []
         }

    # tree, cost = KruskalTree(graph)
    tree = KruskalTree(g).explore_tree()
    print(tree)
