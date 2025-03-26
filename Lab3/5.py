from queue import Queue
from queue import LifoQueue

""" 5 zadatak"""
# 5. Napisati funkciju koja ispituje koliko disjunktnih podgrafova postoji u zadatom neusmerenom
# grafu. Dozvoljeno je više puta pozvati algoritam obilaska grafa. 

def disjoint_subgraphs_count(graph):
    visited = set()
    count = 0
    
    for node in graph:
        if node not in visited:
            # Početak DFS-a za novu komponentu
            stack = LifoQueue()
            stack.put(node)
            visited_local = {node}
            
            while not stack.empty():
                current = stack.get()
                for neighbor in graph[current]:
                    if neighbor not in visited_local:
                        visited_local.add(neighbor)
                        stack.put(neighbor)
            
            # Dodajemo sve posete čvorove u globalni `visited`
            visited.update(visited_local)
            count += 1
    
    return count

# Primer neusmerenog grafa predstavljen kao rečnik
graph = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B'],
    'D': ['E'],
    'E': ['D'],
    'F': []
}

# Pozivanje funkcije i ispis rezultata
num_subgraphs = disjoint_subgraphs_count(graph)
print("Broj disjunktnih podgrafova:", num_subgraphs)
