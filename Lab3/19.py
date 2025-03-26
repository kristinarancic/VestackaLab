from queue import Queue
from queue import LifoQueue

"""19 zadatak"""
# 19. Napisati funkciju koja na osnovu zadatog usmerenog grafa i zadata dva čvora S i M određuje ciklični
# put (takav da ni kroz jedan čvor ne prolazi dva puta) koji počinje i završava se u čvoru S i prolazi
# kroz čvor M. Dozvoljeno je najviše dva puta pozvati prilagođeni algoritam obilaska grafa. 

def cyclic_path_via_m(graph, s, m):
    def dfs_path(start, target):
        stack = LifoQueue()
        stack.put((start, [start]))
        visited = {start}
        
        while not stack.empty():
            node, path = stack.get()
            if node == target:
                return path
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.put((neighbor, path + [neighbor]))
                    # visited.remove(neighbor)
        return None

    path_to_m = dfs_path(s, m)
    if not path_to_m:
        return None

    path_from_m = dfs_path(m, s)
    if not path_from_m:
        return None

    return path_to_m[:-1] + path_from_m

# Definišemo usmereni graf
graph_example = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['A'],
    'E': ['F', 'M'],
    'F': ['A'],
    'M': ['D']
}

# Definišemo usmereni graf
graph_example = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['A'],
    'E': ['F', 'M'],
    'F': ['A'],
    'M': ['D']
}

# Testiranje funkcije
s = 'A'  # Početni i krajnji čvor
m = 'M'  # Čvor kroz koji put mora proći

# Poziv funkcije
cyclic_path = cyclic_path_via_m(graph_example, s, m)
print("Ciklični put koji prolazi kroz čvor M:", cyclic_path)
