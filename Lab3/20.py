from queue import Queue
from queue import LifoQueue

"""20 zadatak"""
# 20. Napisati funkciju koja na osnovu zadatog težinskog neusmerenog grafa i dva zadata (ciljna) čvora
# G1 i G2 formira težinski graf sa heuristikom. Heuristika proizvoljnog čvora C se određuje kao dužina
# puta od čvora C do bližeg od čvorova G1 i G2. Dozvoljeno je najviše dva puta pozvati prilagođeni
# algoritam obilaska grafa. 

def weighted_graph_with_dual_heuristic(graph, g1, g2):
    # BFS sa distancama - koristi FIFO red
    def bfs_distance(start):
        queue = Queue()
        queue.put(start)
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        visited = set()

        while not queue.empty():
            node = queue.get()
            if node in visited:
                continue
            visited.add(node)

            for neighbor, weight in graph[node]:
                # Računanje distance kao prethodne distance + težina ivice
                new_distance = distances[node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    queue.put(neighbor)

        return distances

    # Računanje udaljenosti od oba cilja G1 i G2
    distances_g1 = bfs_distance(g1)
    distances_g2 = bfs_distance(g2)

    # Kreiranje novog grafa sa heuristikama
    result_graph = {}
    for node in graph:
        # Heuristika je minimalna udaljenost do G1 ili G2
        heuristic = min(distances_g1.get(node), distances_g2.get(node))
        # Susedi sa težinama
        neighbors_with_weights = graph[node]
        result_graph[node] = (heuristic, neighbors_with_weights)

    return result_graph

# Testiranje sa težinskim grafom
graph = {
    'A': [('B', 1), ('C', 2)],
    'B': [('A', 1), ('D', 1), ('E', 3)],
    'C': [('A', 2), ('F', 1)],
    'D': [('B', 1)],
    'E': [('B', 3), ('F', 1)],
    'F': [('C', 1), ('E', 1)]
}

print(weighted_graph_with_dual_heuristic(graph, 'A', 'D'))