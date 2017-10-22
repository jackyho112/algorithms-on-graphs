#Uses python3

import sys

def extract_min(queue, dist):
    node = min(queue, key=lambda x: dist[x])

    queue.remove(node)

    return node

def dijkstra(adj, cost, s):
    dist = {}
    prev = {}
    queue = []

    for node in range(len(adj)):
        dist[node] = float("inf")
        prev[node] = None
        queue.append(node)

    dist[s] = 0

    while queue:
        current_node = extract_min(queue, dist)

        edges = adj[current_node]

        for index, target_node in enumerate(edges):
            new_dist = dist[current_node] + cost[current_node][index]
            if dist[target_node] > new_dist:
                dist[target_node] = new_dist
                prev[target_node] = current_node

    return dist

def distance(adj, cost, s, t):
    dist = dijkstra(adj, cost, s)

    if dist[t] < float("inf"):
        return dist[t]

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
