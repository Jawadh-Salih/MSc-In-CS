from node import Node

class Edge :

    vertex1 = Node(0, "")
    vertex2 = Node(0, "")
    def __init__(self, u= Node(1, "M1"), v=Node(1, "U1")):
        self.vertex1 = u
        self.vertex2 = v

    def get_node_pair(self) :
        node_pair = {}
        node_pair[self.vertex1.label] = self.vertex2.label

        return node_pair 