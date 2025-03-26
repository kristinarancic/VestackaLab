from queue import Queue
from queue import LifoQueue

"""11 zadatak"""
# 11. Napisati funkciju koja određuje potege koje je moguće izbaciti iz neusmerenog grafa tako da graf i
# dalje ostane povezan. 

def removable_edges(graph):
    removable = []  # Lista za čuvanje uklonjivih grana

    # Pomoćna funkcija za DFS obilazak grafa bez određene grane
    def dfs(graph, start, skip_edge):
        stack = LifoQueue()
        stack.put(start)
        visited_nodes = {start}  # Novi naziv za set posećenih čvorova unutar DFS-a
        
        while not stack.empty():
            node = stack.get()
            for neighbor in graph[node]:
                # Preskoči granu koju trenutno testiramo za uklanjanje
                if (node, neighbor) == skip_edge or (neighbor, node) == skip_edge:
                    continue
                if neighbor not in visited_nodes:
                    visited_nodes.add(neighbor)
                    stack.put(neighbor)
        
        return visited_nodes  # Vraća skup posećenih čvorova iz DFS-a
    
    # Glavna logika za proveru svake grane
    for node in graph:
        for neighbor in graph[node]:
            # Obrada svake grane samo jednom
            edge = (node, neighbor) if node < neighbor else (neighbor, node)
            if edge in removable:
                continue
            
            # Proveravamo povezanost bez ove grane
            visited_after_removal = dfs(graph, node, edge)
            
            # Ako su svi čvorovi sa susedima poseceni, graf je povezan bez ove grane
            if len(visited_after_removal) == len([n for n in graph]):
                removable.append(edge)

    return removable
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(removable_edges(graph))
