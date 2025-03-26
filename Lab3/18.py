from queue import Queue
from queue import LifoQueue

"""18 zadatak"""
# 18. Napisati funkciju koja na osnovu zadatog usmerenog grafa i zadatog čvora S određuje čvor
# (čvorove) koji su najudaljeniji od njega. Udaljenost se određuje kao dužina najkraćeg puta između
# dva čvora. Dužina puta se određuje kao broj potega koji čine taj put. 

def farthest_nodes_from_s(graph, s):
    queue = Queue()
    queue.put((s, 0))
    visited = {s}
    max_dist = 0
    farthest_nodes = []

    while not queue.empty():
        node, dist = queue.get()
        if dist > max_dist:
            max_dist = dist
            farthest_nodes = [node]#u prvom trenutku kad naidjemo na najvecu duzinu, i kasnije prepisujemo ako nadjemo udaljeniji
        elif dist == max_dist:
            farthest_nodes.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.put((neighbor, dist + 1))

    return farthest_nodes

graph18 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(farthest_nodes_from_s(graph18, 'A'))
