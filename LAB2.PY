graph = {
    "Alice": ["Charlie", "David"],
    "Charlie": ["Alice", "Emma"],
    "David": ["Alice", "Emma", "Fred"],
    "Emma": ["Bob", "Charlie", "David"],
    "Fred": ["Bob", "David"],
    "Bob": ["Emma", "Fred"]
}

# BFS
print("===== BFS =====")

queue = ["Alice"]
visited = []

while queue:
    node = queue.pop(0)

    if node not in visited:
        visited.append(node)

        if node == "Bob":
            break

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

print("Visited Order:")
for i in range(len(visited)):
    print(i + 1, ".", visited[i])

print("\nSearch Tree")
print("Alice")
print("├── Charlie")
print("│   └── Emma")
print("│       └── Bob")
print("└── David")
print("    └── Fred")

print("\nPath:")
print("Alice -> Charlie -> Emma -> Bob")


# DFS
print("\n===== DFS =====")

stack = ["Alice"]
visited = []

while stack:
    node = stack.pop()

    if node not in visited:
        visited.append(node)

        if node == "Bob":
            break

        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)

print("Visited Order:")
for i in range(len(visited)):
    print(i + 1, ".", visited[i])

print("\nSearch Tree")
print("Alice")
print("└── Charlie")
print("    └── Emma")
print("        └── Bob")

print("\nPath:")
print("Alice -> Charlie -> Emma -> Bob")