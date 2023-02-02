from collections import defaultdict as dic

class Breath:
    queue = []
    visited_vertices = []
    def __init__(self):

        self.graph = dic(list)
    
    def add_edge_to_graph(self,x,y):
        self.graph[x].append(y)

    def search(self,n):
        
        self.visited_vertices.append(n)
        self.queue.append(n)
        while self.queue:
            n = self.queue.pop(0)
            print(n,end =" ")

            for v in self.graph[n]:
                if v not in self.visited_vertices:
                    self.queue.append(v)
                    self.visited_vertices.append(v)

if __name__ == '__main__':
    
    graph = Breath()
    graph.add_edge_to_graph(0,1)
    graph.add_edge_to_graph(1,1)
    graph.add_edge_to_graph(2,2)
    graph.add_edge_to_graph(3,1)
    graph.add_edge_to_graph(4,3)
    graph.add_edge_to_graph(5,4)

    graph.search(4)