class Graph:
    def __init__(self, graph, is_undirected=False, store='dict'):
        """
        stores graph in dict.
        exmaple: g = {source: [(dest, weight), (dest1, weight1)]}
        init: Graph(g)

        """
        self.is_undirected = is_undirected
        self.graph = {}  # format: u -> (v,w)

        if isinstance(graph, dict):
            for source in graph:
                try:
                    for destination, weight in graph[source]:
                        self.__add_edge(source, destination, weight)

                except TypeError:
                    # unweighted
                    for destination in graph[source]:
                        self.__add_edge(source, destination, 1)

                except Exception as e:
                    raise(e)

        elif isinstance(graph, list):

            try:
                for source, weights in enumerate(graph2):
                    for destination, weight in enumerate(weights):
                        if source != destination and weight != 0:
                            # if not on diag
                            self.__add_edge(source + 1, destination + 1, weight)

            except Exception as e:
                raise(e)

        else:
            raise(TypeError("Wrong type of graph"))

        self.num_nodes = len(self.graph)
        self.num_edges = self.__get_num_edges()

    def __get_num_edges(self):
        counter = 0
        for edges in self.graph.values():
            counter += len(edges)
        return counter if self.is_undirected else counter // 2

    def __len__(self):
        return self.num_nodes

    def __eq__(self, other):
        return self.graph == other.graph

    def __repr__(self):
        # u -> v(w)
        res = ""
        for u in self.graph:
            res = res + str(str(u) + " -> " + " -> ".join(str(f"{v}({weight})")
                            for v, weight in self.graph[u])) + "\n"
        return res.rstrip()

    def __add_edge(self, u, v, weight):
        #  Edge going from node u to v and v to u with weight
        # u (weight)-> v, v (weight) -> u
        # Check if u already in graph
        if u in self.graph.keys() and (v, weight) not in self.graph[u]:
            self.graph[u].append((v, weight))
        elif u not in self.graph.keys():
            self.graph[u] = [(v, weight)]

        if self.is_undirected:
            if v in self.graph.keys() and (u, weight) not in self.graph[v]:
                self.graph[v].append((u, weight))
            elif v not in self.graph.keys():
                self.graph[v] = [(u, weight)]


if __name__ == '__main__':

    graph1 = {1: [(2, 5), (3, 3)],
              2: []
              }

    print("graph1:", graph1)

    g1 = Graph(graph1, is_undirected=True)
    print(g1)

    print('_' * 40, end='\n\n')

    graph2 = [[0, 5, 3],
              [5, 0, 0],
              [3, 0, 0]]

    print(res, "is res")


    print("graph2:", graph2)

    g2 = Graph(graph2)
    print(g2)

    print("(g1 == g2) is", g1 == g2)  # True

    print(len(g1), "vertexes")  # 3 vertexes
    print(len(g2), "vertexes")  # 3 vertexes
