#Uses python3
import sys
import math

def get_length_between(x, y):
    return ((x[0] - x[1])**2 + (y[0] - y[1])**2)**.5

def extract_min(queue, cost):
    node = min(queue, key=lambda x: cost[x])

    queue.remove(node)

    return node

def minimum_distance(x, y):
    cost = {}
    queue = []

    for i in range(len(x)):
        cost[i] = float("inf")
        queue.append(i)

    cost[0] = 0

    while queue:
        current_node = extract_min(queue, cost)
        for node in queue:
            new_cost = get_length_between(
                [x[current_node], x[node]], [y[current_node], y[node]]
            )

            if new_cost < cost[node]:
                cost[node] = new_cost

    return sum(cost.values())


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
