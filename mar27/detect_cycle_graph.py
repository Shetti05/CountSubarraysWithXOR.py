def dfs(node, parent, visited, adj):
    visited[node] = True
    for neigh in adj[node]:
        if not visited[neigh]:
            if dfs(neigh, node, visited, adj):
                return True
        elif neigh != parent:
            return True
    return False