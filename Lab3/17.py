from queue import Queue
from queue import LifoQueue

"""17 zadatak"""
# 17. Napisati funkciju koja na osnovu zadatog težinskog neusmerenog grafa i zadatog (ciljnog) čvora G
# formira neusmereni težinski graf sa heuristikom. Heuristika proizvoljnog čvora C se određuje kao
# dužina puta od čvora C do čvora G. 

def weighted_graph_with_heuristic(graph, g):
    # Kreiramo red za BFS (iako će ovde biti nešto više nego običan BFS, koristićemo FIFO)
    queue = Queue()
    queue.put((g, 0))  # Početni čvor (ciljni) i udaljenost 0
    distances = {node: float('inf') for node in graph}  # Početne udaljenosti su beskonačnost
    distances[g] = 0  # Udaljenost od ciljnog čvora do sebe je 0
    visited = set()

    while not queue.empty():
        # Uzimamo prvi element iz reda
        node, current_dist = queue.get()

        # Ako smo već posetili ovaj čvor, preskočimo ga
        if node in visited:
            continue
        visited.add(node)

        # Prolazimo kroz susede čvora i ažuriramo udaljenosti
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                new_dist = current_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    queue.put((neighbor, new_dist))

    # Na kraju, vraćamo graf sa heuristikama (udaljenostima) i originalnim susedima
    return {node: (distances[node], [(neighbor, x) for neighbor, x in graph[node]]) for node in graph}

# Testiranje sa težinskim grafom
graph = {
    'A': [('B', 1), ('C', 2)],
    'B': [('A', 1), ('D', 1), ('E', 3)],
    'C': [('A', 2), ('F', 1)],
    'D': [('B', 1)],
    'E': [('B', 3), ('F', 1)],
    'F': [('C', 1), ('E', 1)]
}

print(weighted_graph_with_heuristic(graph, 'F'))
