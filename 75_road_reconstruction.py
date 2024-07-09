nodes_count = int(input())
edges_count = int(input())

graph = []
[graph.append([]) for _ in range(nodes_count)]

edges = []

for _ in range(edges_count):
    first, second = [int(x) for x in input().split(" - ")]
    graph[first].append(second)
    graph[second].append(first)
    edges.append((min(first, second), max(second, first)))

important_streets = []


def dfs(node, graph, visited):
    if visited[node]:
        return
    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited)


for first, second in edges:
    graph[first].remove(second)
    graph[second].remove(first)

    visited = [False] * nodes_count
    dfs(0, graph, visited)

    if not all(visited):
        important_streets.append((first, second))

    graph[first].append(second)
    graph[second].append(first)

print("Important streets:")
for first, second in important_streets:
    print(f'{first} {second}')
