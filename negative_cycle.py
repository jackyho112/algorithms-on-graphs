#Uses python3

import sys

def detect_negative_cycle(adj, cost, dist):
    for current_node in range(len(adj) - 1):
        edges = adj[current_node]

        for index, target_node in enumerate(edges):
            new_dist = dist[current_node] + cost[current_node][index]
            if dist[target_node] > new_dist:
                return 1

    return 0

def bellman_ford(adj, cost):
    num = len(adj)
    dist = {}

    for node in range(num):
        dist[node] = float("inf")

    for target in range(num - 1):
        if dist[target] == float("inf"):
            dist[target] = 0

        for current_node in range(num):
            edges = adj[current_node]

            for index, target_node in enumerate(edges):
                new_dist = dist[current_node] + cost[current_node][index]
                if dist[target_node] > new_dist:
                    dist[target_node] = new_dist

    return dist

def negative_cycle(adj, cost):
    dist = bellman_ford(adj, cost)
    return detect_negative_cycle(adj, cost, dist)

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
    print(negative_cycle(adj, cost))
