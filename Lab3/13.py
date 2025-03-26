from queue import Queue
from queue import LifoQueue

"""13 zadatak"""
# 13. Napisati funkciju koja određuje listu grana u grafu koje je neophodno obrisati da bi se ciklični graf
# transformisao u aciklični (da bi se u njemu eliminisali ciklusi).

def edges_to_remove_cycles(graph):
    visited = set()
    edges_to_remove = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor == parent:#jer je neusmereni graf i sva deca imaju i svog roditelja u listi suseda
                continue
            if neighbor in visited:
                edges_to_remove.add(tuple(sorted((node, neighbor))))
            else:
                dfs(neighbor, node)
    
    for node in graph:
        if node not in visited:
            dfs(node, None)
    
    return edges_to_remove
# Primer grafa
graph_example = {
    'A': ['B', 'C'],
    'B': ['A', 'E', 'D'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C','E']
}


# Pozivanje funkcije - tražimo mostove (kritične grane)
bridges = edges_to_remove_cycles(graph_example)
print("Mostovi (kritične grane):", bridges)
