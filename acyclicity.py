#Uses python3

import sys

def dfs_sink(adj, index, sinks, visited):
    if visited[index]:
        return

    visited[index] = True
    edges = adj[index]

    if len(edges) == 0:
        sinks[index] = True
        return

    for edge in adj[index]:
        if edge not in sinks:
            dfs_sink(adj, edge, sinks, visited)

    if all(sinks[edge] == True for edge in edges):
        sinks[index] = True

def acyclic(adj):
    sinks = [False] * len(adj)
    visited = [False] * len(adj)

    for index, node in enumerate(sinks):
        if visited[index] == False:
            dfs_sink(adj, index, sinks, visited)

    if all(sink == True for sink in sinks):
        return 0

    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
