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
      visited = [False] * (max(self.graph) + 1)
      queue = []
      queue.append(start)
      visited[start] = True
      count_distance = -1
      return_string = " "
      while queue:
         s = queue.pop(0)
         return_string += " " + str(s)
         for i in self.graph[s]:
            if not visited[i]:
               queue.append(i)
               visited[i] = True
            if visited[i]:
               continue
         count_distance += 1
         if count_distance <= distance:
            continue
         if count_distance > distance:
            break
      return return_string

if __name__ == '__main__':

     params = input().rstrip().split()
     start_node =  params[0];
     distance = params[1]
     start_node = int(start_node)
     distance = int(distance)
     first_multiple_input = input().rstrip().split()
     n = int(first_multiple_input[0])
     m = int(first_multiple_input[1])

     g = Graph(n)
     edges = []

     for e in range(m):
        edge = input().rstrip().split()
        res = [int(i) for i in edge]
        g.add_edge(res[0],res[1])

     reachable = g.get_reachable_nodes(start_node, distance)
     print(reachable)
