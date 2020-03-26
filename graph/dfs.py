def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        v = (stack.pop())

        if v in visited:
            continue
        else:
            visited.append(v)

        for w in graph[v]:
            if w not in visited:
                stack.append(w)

    return visited


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

print(dfs(graph, "A"))
