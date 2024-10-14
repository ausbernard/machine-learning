import time
import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(graph, visited, current, target, target_found):
    plt.clf()
    G = nx.Graph()
    pos = {
        0: (0, 0), 1: (1, 0), 2: (2, 0), 3: (3, 0), 4: (4, 0),
        5: (5, 0), 6: (0, 1), 7: (1, 1), 8: (2, 1), 9: (3, 1),
        10: (4, 1), 11: (5, 1), 12: (0, 2), 13: (1, 2), 14: (2, 2),
        15: (3, 2), 16: (4, 2), 17: (5, 2), 18: (0, 3), 19: (1, 3)
    }

    for node, neighbors in enumerate(graph):
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    colors = []
    for node in G.nodes():
        if node == target and target_found:
            colors.append('pink')
        elif visited[node]:
            colors.append('red' if node == current else 'lime')
        else:
            colors.append('blue')

    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=500, font_color='black')
    plt.pause(0.5)

def bfs(graph, start, target, speed):
    visited = [False] * len(graph)
    queue = [start]
    target_found = False

    while queue:
        node = queue.pop(0)
        if not visited[node]:
            visited[node] = True
            draw_graph(graph, visited, node, target, target_found)
            time.sleep(1 / speed)

            if node == target:
                target_found = True
                draw_graph(graph, visited, node, target, target_found)  # Ensure target is highlighted
                return node

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)

    return -1

# Example usage
graph = [
    [1, 6], [0, 2, 7], [1, 3, 8], [2, 4, 9], [3, 5, 10], [4, 11],
    [0, 7, 12], [1, 6, 8, 13], [2, 7, 9, 14], [3, 8, 10, 15],
    [4, 9, 11, 16], [5, 10, 17], [6, 13, 18], [7, 12, 14, 19],
    [8, 13, 15], [9, 14, 16], [10, 15, 17], [11, 16], [12, 19], [13, 18]
]
start_node = 0
target_node = 10
speed = 1.0

plt.ion()
bfs(graph, start_node, target_node, speed)
plt.ioff()
plt.show()