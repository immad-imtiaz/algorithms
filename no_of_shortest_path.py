"""
In social networks analysis it is sometimes useful to find not only the distance between two
vertices in a graph or a shortest path between them, but the number of such paths. It turns
out this problem can be solved efficiently. More precisely, given an undirected graph (no
lengths) G = (V, E) with |V | = n and |E| = m, and two vertices v, w ∈ V , suggest an
algorithm that outputs the number of shortest v − w-paths in G. (The algorithm should not
list all the paths, just the number will do.) The running time of your algorithm should be
O(m + n).
"""

import numpy as np
from collections import deque

# GRAPH
# Adjacency List in dictionary where key is vertex (V) and value is list of edges (E)
# Memory Complexity O( V + E)
graph_adjacency_list = {
    'A': set(['B', 'D', 'E', 'F']),
    'B': set(['A', 'C', 'G']),
    'C': set(['B', 'D', 'E', 'G']),
    'D': set(['A', 'C', 'F']),
    'E': set(['A', 'C']),
    'F': set(['A', 'D']),
    'G': set(['B', 'C'])
}




def bfs_no_of_shortest_path(graph, v, w):
    """
    :param graph: Expects a graph ajacency list
    :param v: The start node
    :param w: The target node
    :return: The number of path between start and target node
    """
    dist = dict()
    total_paths = 0

    for u in graph:
        dist[u] = np.inf  # setting all distance to infinity

    dist[v] = 0
    queue = list(v)

    while not len(queue) == 0:
        # Pop always extract first element with
        # zero input the name might be misleading
        u = queue.pop(0)
        for edge in graph[u]:
                if dist[edge] > dist[u] + 1:
                    dist[edge] = dist[u] + 1
                    queue.append(edge)
                    if edge == w:
                        total_paths += 1
                elif dist[edge] == dist[u] + 1:
                    if edge == w:
                        total_paths += 1
    return total_paths

# No. of path between A and C
print("The total number of shortest paths between Vertex %s and Vertex %s is : %d"
      % ('A', 'C', bfs_no_of_shortest_path(graph_adjacency_list, 'A', 'C')))

# No. of path between C and F
print("The total number of shortest paths between Vertex %s and Vertex %s is : %d"
      % ('C', 'F', bfs_no_of_shortest_path(graph_adjacency_list, 'C', 'F')))

# No. of path between B and d
print("The total number of shortest paths between Vertex %s and Vertex %s is : %d"
      % ('B', 'D', bfs_no_of_shortest_path(graph_adjacency_list, 'B', 'D')))


