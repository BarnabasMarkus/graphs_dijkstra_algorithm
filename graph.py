#!/usr/bin/env python3
# G R A P H S   A N D   D I J K S T R A   A L G O R I T H M

# Project   Graphs and Dijkstra Algorithm
# Author    Barnabas Markus
# Email     barnabasmarkus@gmail.com
# Date      05.08.2016
# Python    3.5.1
# License   MIT

from collections import defaultdict


class Graph():

    def __init__(self, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed

    def add_nodes(self, nodes):
        """ Add nodes to graph """
        for node in nodes:
            self._graph[node] = {}

    def del_nodes(self, nodes):
        """ Delete nodes from graph """
        for node in nodes:
            # delete node
            del self._graph[node]
            # delete edges to node
            for n, e in self._graph.items():
                if node in e:
                    del e[node]

    def add_edges(self, edges):
        """ Add edges to graph """
        for edge in edges:
            # add default weight if no weight given
            weight = 1
            edge = edge if len(edge) == 3 else edge + (weight, )
            n1, n2, w = edge

            # update graph with new nodes if necessary
            for node in n1, n2:
                if node not in self._graph.keys():
                    self._graph[node] = {}

            # update graph with new edge, if directed: 1 way only
            self._graph[n1][n2] = w
            if not self._directed:
                self._graph[n2][n1] = w

    def del_edges(self, edges):
        """ Delete edges from graph """
        for edge in edges:
            n1, n2 = edge
            # del edge, if directed: 1 way only
            del self._graph[n1][n2]
            if not self._directed:
                del self._graph[n2][n1]

    def display(self):
        """ Display graph """
        for node, edges in self._graph.items():
            print(node)
            for edge in edges:
                print(' - ', edge, '(', edges[edge], ')')
            print()

    def nodes(self):
        """ Get nodes """
        return [node for node in self._graph.keys()]

    def edges(self):
        """ Get edges """
        return [[(node, edge, self._graph[node][edge]) for edge in edges]
                for node, edges in self._graph.items()]

    def dijkstra(self, source):
        """ Dijkstra Algorithm """
        
        # dist - node distance from source
        # prev - previous node toward source
        # stack - contains all unvisited nodes
        dist = {node: 10**12 for node in self.nodes()}
        prev = {node: None for node in self.nodes()}
        dist[source] = 0
        stack = {node: 10**12 for node in self.nodes()}

        while stack:
            # pick up a node (u) from stack which has the smallest
            # distance from source and delete it from stack
            u = min([(n, dist[n]) for n in stack], key=lambda x: x[1])[0]
            del stack[u]

            # visit every neighbor of node (u)
            for n in self._graph[u]:
                alt = dist[u] + self._graph[u][n]
                if alt < dist[n]:
                    dist[n] = alt
                    prev[n] = u

        return prev, dist

    def optimal_path(self, src_node, tgt_node):
        """ Get optimal path"""
        prev, cost = self.dijkstra(src_node)
        path = [tgt_node]
        node = tgt_node
        while True:
            path.append(prev[node])
            node = prev[node]
            if node == src_node:
            	break
        return cost[tgt_node], len(path)-1, path[::-1]

# Build test graph
g = Graph()
g.add_nodes([letter for letter in 'ABCDEFG'])
g.add_edges([('A', 'B', 2), ('A', 'C', 5), ('A', 'D', 1), ('A', 'E', 6)])
g.add_edges([('B', 'C', 3)])
g.add_edges([('C', 'D', 2), ('C', 'G', 1)])
g.add_edges([('D', 'F', 2)])
g.add_edges([('E', 'F', 2)])
g.add_edges([('F', 'G', 3)])
