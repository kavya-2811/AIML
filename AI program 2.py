graph = {
    "Alice": sorted(["Charlie", "David"]),
    "Charlie": sorted(["Alice", "Emma"]),
    "David": sorted(["Alice", "Emma", "Fred"]),
    "Emma": sorted(["Bob", "Charlie", "David"]),
    "Fred": sorted(["Bob", "David"]),
    "Bob": sorted(["Emma", "Fred"])
}

def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    parent = {start: None}

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)

            if node == goal:
                break

            # Push in reverse alphabetical order
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    if neighbor not in parent:
                        parent[neighbor] = node
                    stack.append(neighbor)

    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path

print("DFS Path:", dfs(graph, "Alice", "Bob"))