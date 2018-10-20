# This graph has the nodes and edges. 
# Ideally this graph is a set of edges.

from node import Node
from edge import Edge

class Graph :
    # is a set of edges.
    edges = set()
    U = set()
    V = set()

    def __init__(self, U, V) :
        # At very first, there are no edges linked with the Nodes. 
        self.U = U
        self.V = V
        self.edges = set()

    def insert_edge(self, u, v) :
        u.degree = u.degree + 1
        v.degree = v.degree + 1

        e = Edge(u, v)
        # for ee in self.edges : 
        #     if ee.get_node_pair() == e.get_node_pair():
        #         # print(e)
        #         return
            
        self.edges.add(e)
    
    def insert_vertex(self, label) :
        # add a new user to the graph. making vertices constant.
        if ('U' == label) :
            u = Node(0, label + str(len(self.U)))
            self.U.append(u)
            return u
        if ('M' == label) :
            v = Node(0, label + str(len(self.V)))
            self.V.append(v)
            return v

    def print_graph(self) :
        # we should pring all the U,V node pairs
        graph_dict = []
        for e in self.edges :
            graph_dict.append(e.get_node_pair())
        print(graph_dict)
    
    def print_degree_dist(self, V) :
        
        degrees = []
        for v in V:
            degrees.append(v.degree)
        print(degrees)
        