class Graph:
    def __init__(self, size):
        self.size = size
        self.adjmat = []
        for _ in range(size):
            self.adjmat.append([0 for i in range(size)])
    
    def add_edge(self, v1, v2):
        if v1 == v2:
            print("v1 and v2 are referring to the same nodes")
        self.adjmat[v1][v2] = 1
        self.adjmat[v2][v1] = 1
    
    def remove_edge(self, v1, v2):
        if self.adjmat[v1][v2] == 0:
            print("No edge found between %d and %d" % (v1, v2))
            return
        self.adjmat[v1][v2] = 0
        self.adjmat[v2][v1] = 0
    
    def print_matrix(self):
        for row in self.adjmat:
            print(row, sep="  ", end="\n")
        print()


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)

g.print_matrix()

g.remove_edge(0, 1)
g.print_matrix()

