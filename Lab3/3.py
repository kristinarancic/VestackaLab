from queue import Queue
from queue import LifoQueue


""" 3 zadatak"""
# 3. Napisati funkciju koja na osnovu zadatog usmerenog grafa i zadatog (početnog) čvora S formira niz
# čvorova sa njihovim udaljenostima od čvora S. Udaljenost se određuje kao dužina najkraćeg puta
# od čvora A do nekog čvora. Dužina puta se određuje kao broj potega koji čine taj put. 

def distances_from_node(graph, start):
    queue1 = Queue()
    queue1.put((start, 0))
    visited = {start}
    distances = {}
    
    while not queue1.empty():
        node, dist = queue1.get()
        distances[node] = dist
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue1.put((neighbor, dist + 1))
                # visited.add(neighbor)
    
    return distances

# Primer grafa (usmereni graf predstavljen kao rečnik)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(distances_from_node(graph, 'A'))
