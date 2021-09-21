class Graph:
    def __init__(self, vertex):
        self.v = vertex
        self.graph = []
    
    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])
    
    def bellman_ford(self, s):
        # Steps:
        # 1. fill the distance array
        # 2. Mark the source vertex
        # 3. Relax edges |V| - 1 times
        # 4. detect negative cycle
        # 5. If no negative cycle found, then print the distance array
        
        # 1.
        dist = [float("Inf")] * self.v
        # 2.
        dist[s] = 0
        # 3.
        for _ in range (self.v - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
        #4.
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Negative cycle detected")
                return
        #5.
        print("Vertex distance from source")
        for i in range(self.v):
            print("{0}\t\t{1}".format(i, dist[i]))

g = Graph(5)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 4)
g.add_edge(1, 3, 3)
g.add_edge(2, 1, 6)
g.add_edge(3, 2, 2)

g.bellman_ford(0)