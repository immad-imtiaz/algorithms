"""
The square of a directed graph G = (V, E) is the graph G2 = (V, E2
) such that (u, w) ∈ E2
if and only if for some v ∈ V , both (u, v) ∈ E and (v, w) ∈ E. That is, G2
contains an
edge between u and w whenever G contains a path with exactly two edges between u and w.
Describe efficient algorithms for for computing G2
from G for both the adjacency lists and
adjacency matrix representations of G. Analyze the running time of your algorithms.
"""

import numpy as np

# For Adjacency Matrix
G_Matrix = np.array([
    # A  B  C  D  E  F
    [0, 1, 0, 0, 0, 1],  # A
    [1, 0, 1, 0, 0, 0],  # B
    [0, 1, 0, 0, 0, 1],  # C
    [0, 0, 0, 0, 1, 1],  # D
    [0, 0, 0, 1, 0, 1],  # E
    [1, 0, 1, 1, 1, 0]   # F
]).astype(int)


def convert_g_matrix_to_g2_matrix(graph):
    """
    :param graph: Expects graph adjacency matrix
    :return: g2 adjacency matrix
    """
    g2_matrix = np.zeros(graph.shape).astype(int)
    for u_index, u in enumerate(graph):
        for v_index, v in enumerate(u):
            if v == 1:
                for w_index, w in enumerate(graph[v_index]):
                    if w == 1:
                        if u_index != w_index:
                            g2_matrix[u_index][w_index] = 1
    return g2_matrix

matrix_g2 = convert_g_matrix_to_g2_matrix(G_Matrix)

# Input G Adjacency List

G_Adjacency_List = {
    'A': ['B', 'F'],
    'B': ['A', 'C'],
    'C': ['B', 'F'],
    'D': ['E', 'F'],
    'E': ['D', 'F'],
    'F': ['A', 'C', 'D', 'E']
}


def convert_g_adjacency_list_to_g2_adjacency_list(graph):
    """
    :param graph: Expects a graph G adjacency list
    :return: G2 adjacency list
    """
    g2_adjacency_list = dict()
    for u in graph:
        g2_adjacency_list[u] = []

        # To check if a vertex is already added
        added = dict()

        for v in graph[u]:
            for w in graph[v]:
                if w != u and not added.get(w):
                    g2_adjacency_list[u].append(w)
                    added[w] = True
    return g2_adjacency_list

adjacency_list_g2 = convert_g_adjacency_list_to_g2_adjacency_list(G_Adjacency_List)
