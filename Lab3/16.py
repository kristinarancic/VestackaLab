from queue import Queue
from queue import LifoQueue

"""16 zadatak"""
# 16. Napisati funkciju koja na osnovu zadatog usmerenog grafa i zadata tri čvora S, M i G određuje put
# (takav da ni kroz jedan čvor ne prolazi dva puta) od čvora S do čvora G preko čvora M. Dozvoljeno
# je najviše dva puta pozvati prilagođeni algoritam obilaska grafa. 

def path_s_to_g_via_m(graph, s, m, g):
    # Prva BFS pretraga od s do m
    queue1 = Queue()
    queue1.put((s, [s]))
    visited1 = {s}
    path_to_m = None

    while not queue1.empty():
        node, path = queue1.get()
        if node == m:
            path_to_m = path
            break
        for neighbor in graph[node]:
            if neighbor not in visited1:
                visited1.add(neighbor)
                queue1.put((neighbor, path + [neighbor]))

    if path_to_m is None:
        return None

    # Druga BFS pretraga od m do g
    queue2 = Queue()
    queue2.put((m, [m]))
    visited2 = {m}
    path_from_m = None

    while not queue2.empty():
        node, path = queue2.get()
        if node == g:
            path_from_m = path
            break
        for neighbor in graph[node]:
            if neighbor not in visited2:
                visited2.add(neighbor)
                queue2.put((neighbor, path + [neighbor]))

    if path_from_m is None:
        return None

    return path_to_m[:-1] + path_from_m

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(path_s_to_g_via_m(graph, 'A', 'B', 'F'))
