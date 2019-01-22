"""
Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
"""
def connectedTo(graph, start, d):
    if start == d:
        return True
    visited, queue = set(), [start]
    visited.add(start)
    while queue: 
        vertex = queue.pop(0)
        if vertex == d:
            return True
        for neighbour in graph[vertex]:
            if neighbour not in visited: 
                visited.add(neighbour) 
                queue.append(neighbour) 
    return False