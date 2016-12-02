class Vertex:
    def __init__(self,v):
        self.v = v

class Graph:
    vertices = {}
    edge_matrix = []
    label = []

    def add_vertex(self,vertex):
        self.label.append(vertex.v) 
        self.vertices[vertex.v] = len(self.vertices)        
        for i in self.edge_matrix:
            i.append(-1)                     
        self.edge_matrix.append([-1] * (len(self.edge_matrix)+1))   

    def add_edge(self,v1,v2,edge):
        self.edge_matrix[self.vertices[v1]][self.vertices[v2]] = edge  
        self.edge_matrix[self.vertices[v2]][self.vertices[v1]] = edge

    def DIJKSTRA(self,s,d):
        v = s
        for n in self.vertices:
            self.vertices[n] = float("inf")
        self.vertices[s] = 0
        visited = []
        count = 0
        while v != d:
            pos = 0
            for u in self.edge_matrix[self.label.index(v)]:
                if u > 0:
                    if self.vertices[v]+ u < self.vertices[self.label[pos]]:
                        self.vertices[self.label[pos]] = (self.vertices[v]+ u)
                pos += 1        #counts the index
            visited.append(v)
            minimum = float("inf")
            for n in self.label:
                if n not in visited and self.vertices[n] < minimum:
                    v = n
                    minimum = self.vertices[n]
            print("current",v,"goal",d)
            print(self.vertices)

if __name__ == '__main__':
    g = Graph()
    g.add_vertex(Vertex("A"))
    g.add_vertex(Vertex("B"))
    g.add_vertex(Vertex("C"))
    g.add_vertex(Vertex("D"))
    g.add_vertex(Vertex("E"))
    g.add_vertex(Vertex("F"))
    g.add_vertex(Vertex("G"))
    g.add_edge("A","B",3)
    g.add_edge("B","D",4)
    g.add_edge("A","E",1)
    g.add_edge("B","F",3)
    g.add_edge("A","C",2)
    g.add_edge("C","G",1)
    g.add_edge("E","F",5)
    g.add_edge("G","F",2)
    for i in range(0,len(g.edge_matrix)):
        print(g.label[i],g.edge_matrix[i])
    g.DIJKSTRA("A","F")


