
### 2. `main.py`

```python
"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""

def longest_path(graph: list) -> int:
    n = len(graph)
    
    #sorting using DFS
    def topological_sort():
        visited = [False] * n
        topo_order = []
        
        def dfs(node):
            visited[node] = True
            for neighbor, weight in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
            topo_order.append(node)
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
        
        topo_order.reverse()
        return topo_order
    
    topo_order = topological_sort()
    
    # Initialize distances
    dist = [-float('inf')] * n
    dist[topo_order[0]] = 0
    
    #Process nodes in topological order 
    for u in topo_order:
        if dist[u] != -float('inf'):  # Only process reachable nodes
            for v, weight in graph[u]:
                if dist[v] < dist[u] + weight:
                    dist[v] = dist[u] + weight
    
    # Finding the maximum distance
    max_distance = max(dist)
    
    return max_distance
