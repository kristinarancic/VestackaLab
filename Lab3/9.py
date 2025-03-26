from queue import Queue
from queue import LifoQueue

""" 9 zadatak"""
# 9. Napisati funkciju koja određuje broj čvorova do kojih može da se dođe od zadatog čvora, tako da
# je dužina puta do čvora jednaka zadatoj vrednosti. Obići samo neophodne čvorove.

def nodes_at_distance(graph, start, target_distance):
    queue = Queue()
    queue.put((start, 0))#udaljenost od samog sebe
    visited = {start}
    count = 0
    
    while not queue.empty():
        node, dist = queue.get()
        if dist == target_distance:
            count += 1
        elif dist < target_distance:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.put((neighbor, dist + 1))
    
    return count
# Primer neusmerenog grafa
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['C', 'E', 'H'],
    'H': []
}

# Primer pokretanja funkcije
start_node = 'A'
target_distance = 3
result = nodes_at_distance(graph, start_node, target_distance)
print(f"Broj čvorova na udaljenosti {target_distance} od čvora {start_node} je: {result}")
