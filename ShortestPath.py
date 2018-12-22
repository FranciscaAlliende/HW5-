
def BFS_prev(graph, S):
    prev = {}
    # visited nodes
    visited = []
    # Query
    Q = []
    # First we append the node S on the query
    Q.append(S)
    # While we have nodes on query:
    while Q:
        current = Q.pop()
        for child in graph[current]:
            if child not in visited: # havent been discovered jet
                Q = Q + list(child)
                visited.append(child)
                prev[child] = current
    return prev

def ShortestPath(S, F, graph):
    # Previous nodes dictionary
    D = BFS_prev(graph, S)
    path = []
    # If S = F return 0
    if S == F:
        return len(path) 
    # If the node F is not conected in any way with S, then pass
    elif F not in D:
        pass
    # Otherwise, computhe the path, following the previous nodes, backwards
    else:
        C = F
        while C != S:
            path.append(D[C])
            C = D[C]
        return len(path)