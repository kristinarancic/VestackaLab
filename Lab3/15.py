from queue import Queue
from queue import LifoQueue

"""15 zadatak"""
# 15. Napisati funkciju koja proverava da li graf sadrži Ojlerov put (put kojim se obilazi celokupan graf,
# uz obilazak svake grane tačno jednom).

def has_eulerian_path(graph, start):
    
    # Provera povezanosti grafa pomoću BFS
    queue = Queue()
    queue.put(start)
    visited = {start}
    
    while not queue.empty():
        node = queue.get()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.put(neighbor)

    # Proveri da li smo posetili sve čvorove sa susedima, ako nismo graf nije povezan, pa nema Ojlerov put
    for node in graph:
        if graph[node] and node not in visited:  # Čvor ima susede, ali nije posećen
            return False  # Graf nije povezan

    # Brojanje čvorova sa neparnim stepenom
    odd_degree_nodes = 0
    for node in graph:
        if len(graph[node]) % 2 != 0:
            odd_degree_nodes += 1

    # Ojlerov put postoji ako graf ima 0 ili 2 čvora sa neparnim stepenom, po teoremi
    return odd_degree_nodes == 0 or odd_degree_nodes == 2
# Primer grafa
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'B', 'E'],
    'D': ['B', "F"],
    'E': ['C', 'F'],
    'F': ['E']
} #ima
graph1 = {
    'A': ['B'],
    'B': ['A', 'E'],
    'C': ['D'],
    'D': ['C'],
    'E': ['B']
} #nema

# Pozivanje funkcije
if has_eulerian_path(graph, 'A'):
    print("Graf ima Ojlerov put.")
else:
    print("Graf nema Ojlerov put.")
