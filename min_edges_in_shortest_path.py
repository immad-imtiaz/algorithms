"""
In cases where there are several different shortest paths between two nodes (and edges have
varying lengths), the most convenient of these paths is often the one with fewest edges.
Accordingly, for a specific starting node s, define
best[u] = minimum number of edges in a shortest path from s to u.
Give an efficient algorithm for the following problem
Input: Graph G = (V, E), positive edge lengths `e, starting node s ∈ V .
Output: The values of best[u] for all vertices u ∈ V .
"""

import heapq
import numpy as np
from collections import defaultdict

edges = [
    (2, ("A", "B")),
    (2, ("A", "D")),
    (1, ("A", "C")),
    (3, ("B", "E")),
    (4, ("C", "F")),
    (3, ("D", "F")),
    (3, ("E", "D")),
]



def dijkstra_for_best_values(graph_edges, s):
    """
    :param graph_edges:  (positive edge lengths, Graph G = (V, E))
    :param s: Starting Node s
    :return: The values of best[u] for all vertices u
    """
    dist = dict()
    best = dict()
    # graph table to maintain adjacency list
    # default dict is like a normal dict
    # returns empty adjacency list if no key
    graph = defaultdict(list)

    for c, (u, v) in graph_edges:
        # Since we have the edge list we do the
        # below for both u and v as graph is
        # direct edges are not repeated
        best[u] = 0
        best[v] = 0
        dist[u] = np.inf
        dist[v] = np.inf
        graph[u].append(v)   # making an adjacency list

    dist[s] = 0
    # Make binary heap as the start node
    # Distance for start node is 0
    h = []
    for c, (u, v) in graph_edges:
        # Queue contains dist, vertex and path
        h.append((dist[u], u))
        heapq.heapify(h)

    while len(h) != 0:  # while H is not empty
        (cost, u) = heapq.heappop(h)  # same as delete-min for binary heap
        for v in graph[u]:
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                heapq.heappush(h, (dist[u] + c, v))
                best[v] = best[u] + 1
            if dist[v] == dist[u] + cost:
                if best[v] > best[u] + 1:
                    best[v] = best[u] + 1
    return best


a = dijkstra_for_best_values(edges, 'A')