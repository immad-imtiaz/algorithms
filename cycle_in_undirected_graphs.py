"""
Give an algorithm to detect whether a given undirected graph contains a cycle. If the graph
contains a cycle, then your algorithm should output one (not all). The running time of your
algorithm should be O(m + n) for a graph with n vertices and m edges.
"""



# GRAPH
# Adjacency List in dictionary
# where key is vertex (V)
# and value is list of edges (E)
# Memory Complexity O( V + E)
graph_adjacency_list = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'E']),
    'D': set(['B', 'E', 'F']),
    'E': set(['B', 'C', 'D', 'F']),
    'F': set(['D', 'E'])
}


def explore(v, graph, visited, parent, back_edge, back_edge_found):
    """
    :param v: The vertex to explore
    :param graph: Graph adjacency list
    :param visited: Visited maker for all vertices
    :param parent: Parent record for all vertices
    :param back_edge: Records for back edge found which denotes a cycle
    :param back_edge_found: A flag to keep record of a back edge found
    :output: visited is marked to True for all edges u reachable from u,
    also records first back edge encountered and set back_edge_found to true
    """
    visited[v] = True
    for u in sorted(graph[v]):
        if not visited[u]:
            # for each non visited adjacent node we do DFS explore
            parent[u] = v
            explore(u, graph, visited, parent, back_edge, back_edge_found)
        else:
            # if an adjacent node is already visited and is not parent of the node
            # then it denotes that a cycle exist in graph

            # we only need to find one back edge as we only need one cycle path
            if u != parent[v] and parent[v] is not None and not back_edge_found['found']:
                # Since undirected we are considering it twice as one path might
                # have root node that result in no parent,
                # hence we will get reverse path considering in
                # other direction
                back_edge.append((u, v))
                back_edge.append((v, u))
                back_edge_found['found'] = True


def dfs(adjacency_list):
    visited = dict()  # Keep track of visited nodes
    parents = dict()  # Keep track of parent nodes
    back_edge = []  # Contains the cycle found

    # Just a dict to keep track if the cycle is found,
    # as boolean variable is passed by value in python
    # we need by reference
    cycle_found = {'found': False}

    for v in adjacency_list:
        parents[v] = None
        visited[v] = False

    # Visit through all the vertices once
    for v in sorted(adjacency_list.keys()):
        if not visited[v]:
            # In second iteration a vertex would be not
            #  visited if it belong to another component
            explore(v, adjacency_list, visited, parents, back_edge, cycle_found)
    return visited, parents, back_edge


# Complexity: O(2V)
def print_path_for_back_edge(back_edge, parent):
    """
    :param back_edge: A back edge (u,v) given as [(u,v), (v,u)] as graph is undirected
    :param parent: table that maintains parents of each edge found in DFS
    :return: Prints
    """
    # runs twice as back_edge is suppose to have length 2
    for edges in back_edge:
        v, u = edges
        current = v
        path = []
        gets_completed = True
        # expected to go till the maximum possible
        # height of the tree in worst case
        # which can be O(V)
        while current != u:
            path.append(current)
            current = parent.get(current)
            # current can be none if path contains the root node
            # hence we just ignore those path as we get the reverse
            # path in case of undirected graphs for the same cycle
            if current is None:
                gets_completed = False
                break
        if gets_completed:
            path.append(current)
            path.append(v)
            print("Cycle path in graph is %s" % "->".join(path))

all_visited, all_parents, back_edges = dfs(graph_adjacency_list)
print_path_for_back_edge(back_edges, all_parents)

# Total Complexity: O(V + E) (DFS) + O(2V) = O(V+E)

