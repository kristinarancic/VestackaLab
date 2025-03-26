from queue import Queue
from queue import LifoQueue

"""8 zadatak"""
# 8. Napisati funkciju koja određuje put između zadatog polaznog i ciljnog čvora neusmerenog grafa
# tako što istovremeno pokreće traženje po širini od polaznog i od ciljnog čvora. Traženje se završava
# kada se nađe prvi zajednički čvor za oba traženja.

def bidirectional_bfs(graph, start, end):
    if start == end:
        return [start]

    queue_start, queue_end = Queue(), Queue()
    queue_start.put((start, [start]))#ovo drugo je put(path) 
    queue_end.put((end, [end]))
    visited_start, visited_end = {start: [start]}, {end: [end]}
    
    def expand(queue, visited, other_visited):
        node, path = queue.get()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited[neighbor] = path + [neighbor]
                queue.put((neighbor, visited[neighbor]))
            if neighbor in other_visited:
                return neighbor
        return None

    while not queue_start.empty() and not queue_end.empty():
        intersect = expand(queue_start, visited_start, visited_end)
        if intersect:
            # return visited_start[intersect][:-1] + visited_end[intersect][::-1]
            return visited_start[intersect][:-1] + list(reversed(visited_end[intersect]))
        # intersect = expand(queue_end, visited_end, visited_start)
        # if intersect:
        #     return visited_start[intersect][:-1] + visited_end[intersect][::-1]
    
    return None
# Primer neusmerenog grafa
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

# Testiranje sa polaznim i ciljnim čvorom
start = 'A'
target = 'J'
path = bidirectional_bfs(graph, start, target)

if path:
    print(f"Put između '{start}' i '{target}': {' -> '.join(path)}")
else:
    print(f"Nema puta između '{start}' i '{target}'.")
