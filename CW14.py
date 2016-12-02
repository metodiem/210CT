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
            i.append(False)
        self.edge_matrix.append([False] * (len(self.edge_matrix)+1))

    def add_edge(self,v1,v2,edge=True):
        self.edge_matrix[self.vertices[v1]][self.vertices[v2]] = edge
        self.edge_matrix[self.vertices[v2]][self.vertices[v1]] = edge

    def DFS(self,vertex):
        stack = []
        visited = []
        stack.append(vertex)
        while len(stack) > 0:
            u = stack.pop()
            if u not in visited:
                visited.append(u)
                pos = 0
                for e in self.edge_matrix[self.vertices[u]]:
                    if e == True:
                        stack.append(self.label[pos])
                    pos += 1
        return visited
    
    def BFS(self,vertex):
        queue = []
        visited = []
        queue.append(vertex)
        while len(queue) > 0:
            u = queue.pop(0)
            if u not in visited:
                visited.append(u)
                pos = 0
                for e in self.edge_matrix[self.vertices[u]]:
                    if e == True:
                        queue.append(self.label[pos])
                    pos += 1
        return visited
                    
if __name__ == '__main__':
    g = Graph()
    g.add_vertex(Vertex("A"))
    g.add_vertex(Vertex("B"))
    g.add_vertex(Vertex("C"))
    g.add_vertex(Vertex("D"))
    g.add_vertex(Vertex("E"))
    g.add_vertex(Vertex("F"))
    g.add_vertex(Vertex("G"))
    g.add_edge("A","B")
    g.add_edge("B","D")
    g.add_edge("A","E")
    g.add_edge("B","F")
    g.add_edge("A","C")
    g.add_edge("C","G")
    g.add_edge("E","F")
    DFS = g.DFS("A")
    BFS = g.BFS("A")
    for i in range(0,len(g.edge_matrix)):
        print(g.label[i],g.edge_matrix[i])
    file = open("Traversals.txt","w")
    file.write("DFS:" + str(DFS) + "\n")
    file.write("BFS:" + str(BFS))
    file.close()
