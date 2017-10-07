#Uses python3

import sys

def explore(adj, node, visited, order):
    visited[node] = True
    for edge in adj[node]:
        if not visited[edge]:
            explore(adj, edge, visited, order)
    order.append(node)

def toposort(adj):
    visited = [False] * len(adj)
    order = []

    for index, node in enumerate(visited):
        if not node:
            explore(adj, index, visited, order)

    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[b - 1].append(a - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')
