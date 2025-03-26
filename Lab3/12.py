from queue import Queue
from queue import LifoQueue

"""12 zadatak"""
# 12. Napisati funkciju koja pronalazi puteve zadate dužine u neusmerenom grafu između dva zadata
# čvora.

def paths_of_length(graph, start, end, length):
    def dfs(node, path_length, visited):
        if path_length == length:
            return 1 if node == end else 0
        count = 0
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                count += dfs(neighbor, path_length + 1, visited)
                visited.remove(neighbor)#da ne bismo opet prolazili kroz iste stvari
        return count

    return dfs(start, 0, {start})
# Primer grafa
graph_example = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'E'],
    'D': ['B'],
    'E': ['C', 'F'],
    'F': ['E']
}

# Pozivanje funkcije - tražimo sve puteve dužine 3 između A i F
duzina=3
cvor1='A'
cvor2='D'
paths = paths_of_length(graph_example, cvor1, cvor2, duzina)
print(f"Putevi duzine {duzina} izmedju {cvor1} i {cvor2}: {paths}")
