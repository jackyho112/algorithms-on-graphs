#Uses python3

import sys
import queue

def bfs(adj, s):
    dist = {}
    prev = {}
    localQueue = queue.Queue()

    for i in range(len(adj)):
        dist[i] = False
        prev[i] = []

    dist[s] = 0
    localQueue.put(s)

    while not localQueue.empty():
        current = localQueue.get()
        for nextNode in adj[current]:
            if dist[nextNode] == False:
                localQueue.put(nextNode)
                dist[nextNode] = dist[current] + 1
                prev[nextNode].append(current)

    return prev

def find_distance(prev, s, t):
    if not prev[t]:
        return -1

    distance = 0
    result = []
    current = [t]
    while s not in result:
        local_current = []
        distance += 1

        for last in current:
            result.append(last)
            local_current += prev[last]

        current = local_current

    return distance - 1

def distance(adj, s, t):
    prev = bfs(adj, s)

    return find_distance(prev, s, t)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
