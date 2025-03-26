from queue import Queue
from queue import LifoQueue

"""14 zadatak"""
# 14. Napisati funkciju koja određuje da li je usmereni graf jako povezan graf (da li postoji put između
# bilo koja dva čvora u grafu).

def is_strongly_connected(graph):
    def dfs(start):
        stack = LifoQueue()
        stack.put(start)
        visited = {start}
        
        while not stack.empty():
            node = stack.get()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.put(neighbor)
        return visited

    all_nodes = set(graph.keys())
    for node in graph:
        if dfs(node) != all_nodes:
            return False
    
    return True
# Primer: Usmereni graf sa slovnim oznakama čvorova
graph = {
    'A': ['B', 'D'],
    'B': ['C', 'E'],
    'C': ['F'],
    'D': ['A'],
    'E': ['D', 'F'],
    'F': ['E']
}

graph1 = {
    'A': ['B'],
    'B': ['C'],
    'C': ['F'],
    'D': ['A'],
    'E': [],
    'F': ['E']
}

# Poziv funkcije
if is_strongly_connected(graph):
    print("Graf je jako povezan.")
else:
    print("Graf nije jako povezan.")
