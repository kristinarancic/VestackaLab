from queue import Queue
from queue import LifoQueue

""" 2 zadatak"""
# 2. Napisati funkciju koja određuje broj disjunktnih puteva između dva zadata čvora u grafu. Rešenje
# ne mora biti optimalno prema broju puteva. Dozvoljeno je više puta pozvati algoritam obilaska
# grafa. 

def disjoint_paths_count(graph, start, end):
    def dfs(node, visited):
        if node == end:
            return 1
        count = 0
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                count += dfs(neighbor, visited)
                visited.remove(neighbor)
        return count
    
    return dfs(start, {start})

# Primer grafa
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Pozivanje funkcije sa primerom startnog i ciljnog čvora
start_node = 'A'
end_node = 'F'

print("Broj disjunktnih puteva:", disjoint_paths_count(graph, start_node, end_node))
