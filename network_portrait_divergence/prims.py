# Copyright 2021, Hiun Shim, All rights reserved.

from collections import defaultdict
import heapq
import math
import random
import networkx as nx
from zss import Node

# Randomly generate a graph for example
def generate_random_coordinates(n):
    random_coordinates = {}
    i = 0
    # Random vertices
    while i < n:
        random_coordinates[i] = (random.randint(-10*n, 10*n), random.randint(-10*n, 10*n))
        i += 1
    return random_coordinates # {0: (x,y), 1:(x,y), 2:(x,y)}

def generate_graph_distance(vertices):
    distances = {}
    for u in vertices:
        edges = {}
        for v in vertices:
            if v in distances:
                edges[v] = distances[v][u]
            else:
                distance = math.sqrt((vertices[v][0]-vertices[u][0])**2 + (vertices[v][1]-vertices[u][1])**2)
                edges[v] = distance
        distances[u] = edges 
    return distances # {0: {0: 0-0 distance, 1: 0-1 distance, 0-2 distance}, 1: {1: 1-1 distance, 2: 1-2 distance}}

def create_spanning_tree(graph, starting_vertex):
    mst = defaultdict(set)
    visited = set([starting_vertex])
    edges = [
        (cost, starting_vertex, to)
        for to, cost in graph[starting_vertex].items()
    ]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst[frm].add(to)
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))
    return mst # {0: {3, 5}, 3: {2, 6}, 2: {8, 1}, 8: {9}, 1: {4}, 4: {7}, 9: set(), 7: set(), 6: set(), 5: set()} 

# Plot the coordinates based on the MST
def generate_coordinates_connections(tree, vertices):
    coordinates = []
    for u in tree:
        for v in tree[u]:
            coordinates.append([vertices[u], vertices[v]])
    return coordinates # [[(2, 10), (5, 9)], [(5, 9), (9, 7)]]

def generate_graph(tree, coordinates):
    distances = generate_graph_distance(coordinates)
    graph = nx.Graph()
    for u in tree:
        graph.add_node(u, pos=coordinates[u])
        for v in tree[u]:
            graph.add_node(v, pos=coordinates[v])
            graph.add_edge(u, v, weight=distances[u][v])
    return graph

def generate_zss(tree, node):
    temp = Node(node)
    for child in tree[node]:
        temp.addkid(generate_zss(tree, child))
    return temp
