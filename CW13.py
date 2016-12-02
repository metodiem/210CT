class Vertex:
    def __init__(self,v):
        self.v = v

class Graph:
    vertices = {}
    edge_matrix = []
    label = []

    def add_vertex(self,vertex):
        self.label.append(vertex.v)                         #stores the label of the vertex
        self.vertices[vertex.v] = len(self.vertices)        #stores the vertices
        for i in self.edge_matrix:
            i.append(False)                                 #adds a 0 to every existing row of the matrix
        self.edge_matrix.append([False] * (len(self.edge_matrix)+1))   #adds a new row of 0's

    def add_edge(self,v1,v2,edge=True):
        self.edge_matrix[self.vertices[v1]][self.vertices[v2]] = edge  #Creates an edge from v1 to v2
        self.edge_matrix[self.vertices[v2]][self.vertices[v1]] = edge  #Creates an edge from v2 to v1
        

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
    for i in range(0,len(g.edge_matrix)):
        print(g.label[i],g.edge_matrix[i])
    

'''
CLASS VERTEX
    v <- v
    
CLASS GRAPH
    vertices <- new dict()
    edge_matrix <- []
    llabel <- []
    
    ADD_VERTEX(vertex)
    
        label.append(vertex)
        add vertex.v as vertices.size in vertices
        for all rows in edge_matrix, rows.append(False)
        edge_matrix.append(False * edge_matrix.size+1)

    ADD_EDGE(v1,v2,True)
        edge_matrix[vertices[v1][vertices[v2]] = True
        edge_matrix[vertices[v2][vertices[v1]] = True
    
'''
