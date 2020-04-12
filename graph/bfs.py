#!/usr/bin/env python3

def bfs(graph, start):
    visited = [start]
    queue = [start]

    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                queue.append(w)

    return visited


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    print(bfs(graph, "A"))
