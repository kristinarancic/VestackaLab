from queue import Queue
from queue import LifoQueue

"""7 zadatak"""
# 7. Napisati funkciju koja na osnovu zadatog neusmerenog grafa i dva zadata (ciljna) čvora G1 i G2
# formira neusmereni graf sa heuristikom. Heuristika proizvoljnog čvora C se određuje kao
# udaljenost čvora C do bližeg od čvorova G1 i G2. Udaljenost se određuje kao dužina najkraćeg puta
# između dva čvora. Dužina puta se određuje kao broj potega koji čine taj put. Dozvoljeno je najviše
# dva puta pozvati prilagođeni algoritam obilaska grafa. 

def heuristic_graph_dual(graph, g1, g2):
    def bfs_distance(start):
        queue = Queue()#moze i Stack tj LifoQueue
        queue.put((start, 0))
        visited = {start}
        distances = {}#dict
        
        while not queue.empty():
            node, dist = queue.get()
            distances[node] = dist
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.put((neighbor, dist + 1))
        
        return distances

    distances_g1 = bfs_distance(g1)
    distances_g2 = bfs_distance(g2)
    return {node: (min(distances_g1.get(node), distances_g2.get(node)), graph[node]) for node in graph}
# Primer neusmerenog grafa
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(heuristic_graph_dual(graph, 'D', 'F'))
