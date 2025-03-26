from queue import Queue
from queue import LifoQueue
""" 1 zadatak"""
# 1. Napisati funkciju koja određuje visinu stabla traženja (broj nivoa u stablu traženja), za algoritam
# obilaska grafa po širini, koje se formira za zadati polazni čvor i zadati graf. 

def bfs_tree_height(graph, start):
    queue1 = Queue()
    queue1.put((start, 0))
    visited = {start}
    max_level = 0

    while not queue1.empty():
        node, level = queue1.get()
        max_level = max(max_level, level)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue1.put((neighbor, level + 1))
    
    return max_level

# Testiranje
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['G', 'I'],
    'F': ['J'],
    'G': ['J'],
    'H': [],
    'I': ['J'],
    'J': []
}
graph1 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
height = bfs_tree_height(graph1, start_node)
print(f"Visina stabla traženja od čvora {start_node} je: {height}")
