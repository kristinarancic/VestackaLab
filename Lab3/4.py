from queue import Queue
from queue import LifoQueue

""" 4 zadatak"""
# 4. Napisati funkciju koja na osnovu zadatog neusmerenog grafa i zadatog (ciljnog) čvora G formira
# neusmereni graf sa heuristikom. Heuristika proizvoljnog čvora C se određuje kao udaljenost čvora
# C od čvora G. Udaljenost se određuje kao dužina najkraćeg puta između dva čvora. Dužina puta se
# određuje kao broj potega koji čine taj put. 

def heuristic_graph(graph, g):
    queue = Queue()
    queue.put((g, 0))
    visited = {g}
    distances = {}

    while not queue.empty():
        node, dist = queue.get()
        distances[node] = dist
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.put((neighbor, dist + 1))

    heuristic_graph = {node: (distances[node], graph[node]) for node in graph}
    return heuristic_graph
# Primer neusmerenog grafa predstavljen kao rečnik
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
    'G': ['E', 'F']
}

# Zadatak ciljni čvor
goal_node = 'G'

# Pozivanje funkcije i ispis rezultata
heuristic_graph_with_heuristics = heuristic_graph(graph, goal_node)
print(heuristic_graph_with_heuristics)
# print("Graf sa heuristikama u obliku (susedi, heuristika) u odnosu na ciljni čvor", goal_node)
# for node, data in heuristic_graph_with_heuristics.items():
#     print(f"{node}: {data}")
