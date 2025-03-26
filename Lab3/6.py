from queue import Queue
from queue import LifoQueue


"""6 zadatak"""
# 6. Napisati funkciju koja formira stablo traženja za zadati graf, zadati polazni čvor i izabrani algoritam
# koji se koristiti za obilazak stabla. Student sam bira algoritam za koji se formira stablo traženja. 

def search_tree(graph, start, algorithm="bfs"):
    tree = {start: []}
    visited = {start}
    container = Queue() if algorithm == "bfs" else LifoQueue()
    container.put((start, None))#(cvor, njegov roditelj)
    
    while not container.empty():
        node, parent = container.get()
        if parent is not None:
            tree[parent].append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                container.put((neighbor, node))
                tree[node] = tree.get(node, [])
    
    return tree

# Primer korišćenja
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'

# Formiranje stabla traženja iz čvora 'A' korišćenjem BFS-a
tree_bfs = search_tree(graph, start_node, algorithm="bfs")
print("Stablo traženja (BFS):", tree_bfs)

# Formiranje stabla traženja iz čvora 'A' korišćenjem DFS-a
tree_dfs = search_tree(graph, start_node, algorithm="dfs")
print("Stablo traženja (DFS):", tree_dfs)
