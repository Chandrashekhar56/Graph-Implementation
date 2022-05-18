class Node_of_AdjacencyList:
    def __init__(self, item):
        self.vertex_data = item
        self.next_part = None

class graph_class:

    def __init__(self, total_vertices):
        self.total_vertices = total_vertices
        self.graph = [None] * self.total_vertices

    def Add_New_Edge(self, source_vertex, destination_vertex):
        new_node = Node_of_AdjacencyList(destination_vertex)
        new_node.next_part = self.graph[source_vertex]
        self.graph[source_vertex] = new_node

        new_node = Node_of_AdjacencyList(source_vertex)
        new_node.next_part = self.graph[destination_vertex]
        self.graph[destination_vertex] = new_node

    def display(self):
        for x in range(self.total_vertices):
            print ('Adjacency list of vertex: ')
            print ("source_vertex: {} ".format(x))
            temporary = self.graph[x]
            while temporary:
                print ("destination vertex: ==> {}".format(temporary.vertex_data))
                temporary = temporary.next_part
            print ("\n")


if __name__ == '__main__':
    total_vertices = 5
    ob = graph_class(total_vertices)
    ob.Add_New_Edge(0, 1)
    ob.Add_New_Edge(0, 4)
    ob.Add_New_Edge(1, 2)
    ob.Add_New_Edge(1, 3)
    ob.Add_New_Edge(3, 2)
    ob.Add_New_Edge(4, 1)
    ob.Add_New_Edge(3, 4)
    ob.display()
