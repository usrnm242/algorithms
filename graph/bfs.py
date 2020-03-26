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


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}


if __name__ == "__main__":
    print(bfs(graph, "A"))