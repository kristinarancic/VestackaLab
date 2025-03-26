from queue import Queue
from queue import LifoQueue

"""10 zadatak"""
# 10. Napisati funkciju koja pronalazi put u neusmerenom grafu između dva zadata čvora, pri čemu put
# prolazi kroz treći zadati čvor.

def path_via_node(graph, start, middle, end):
    # BFS od start do middle
    queue1 = Queue()
    queue1.put((start, [start]))
    visited1 = {start}
    path_to_middle = None

    while not queue1.empty():
        node, path = queue1.get()
        if node == middle:
            path_to_middle = path
            break
        for neighbor in graph[node]:
            if neighbor not in visited1:
                visited1.add(neighbor)
                queue1.put((neighbor, path + [neighbor]))

    if path_to_middle is None:
        return None

    # BFS od middle do end
    queue2 = Queue()
    queue2.put((middle, [middle]))
    visited2 = {middle}
    path_from_middle = None

    while not queue2.empty():
        node, path = queue2.get()
        if node == end:
            path_from_middle = path
            break
        for neighbor in graph[node]:
            if neighbor not in visited2:
                visited2.add(neighbor)
                queue2.put((neighbor, path + [neighbor]))

    if path_from_middle is None:
        return None

    return path_to_middle[:-1] + path_from_middle

#drugo resenje, s dve funkcije

def bfs(graph, start, goal):
    """Generalizovana funkcija za BFS koja traži put od start do goal."""
    queue = Queue()
    queue.put((start, [start]))
    visited = {start}
    
    while not queue.empty():
        node, path = queue.get()
        if node == goal:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.put((neighbor, path + [neighbor]))
    
    return None  # Ako nije pronađen put

def path_via_node(graph, start, middle, end):
    # Pronađi put od start do middle
    path_to_middle = bfs(graph, start, middle)
    if path_to_middle is None:
        return None
    
    # Pronađi put od middle do end
    path_from_middle = bfs(graph, middle, end)
    if path_from_middle is None:
        return None

    # Kombinuj put do middle (bez middle na kraju) i put od middle do end
    return path_to_middle[:-1] + path_from_middle

# Testiranje
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'H'],
    'E': ['B', 'G', 'I'],
    'F': ['C', 'J'],
    'G': ['C', 'E', 'J'],
    'H': ['D'],
    'I': ['E', 'J'],
    'J': ['F', 'G', 'I']
}

start = 'A'
middle = 'C'
end = 'J'

# Poziv funkcije
result = path_via_node(graph, start, middle, end)
print(result)  # Trebalo bi da ispise put kroz čvor 'B'
