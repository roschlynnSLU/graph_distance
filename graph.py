# Python3 Program to print breadth_first_search traversal
# from a given source vertex. breadth_first_search(int s)
# traverses vertices reachable from s.

# This class represents a directed graph
# using adjacency list representation


class Graph:

   # Constructor
   def __init__(self, num_vertices):

      # default dictionary to store graph
      self.graph = {}
      self.num_vertices = num_vertices

   # function to add an edge to graph
   def add_edge(self, u, v):
      if not u in self.graph:
         self.graph[u] = [v]
      else:
         self.graph[u].append(v)

   def get_reachable_nodes(self, start, distance):
      print(self.graph)
      pass


if __name__ == '__main__':

     params = input().rstrip().split()
     start_node =  params[0];
     distance = params[1]
     first_multiple_input = input().rstrip().split()
     n = int(first_multiple_input[0])
     m = int(first_multiple_input[1])

     g = Graph(n)
     edges = []

     for e in range(m):
        edge = input().rstrip().split()
        g.add_edge(edge[0],edge[1])

     reachable = g.get_reachable_nodes(start_node, distance)
