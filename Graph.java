// Java program to print breadthFirstSearch traversal from a given source
// vertex. breadthFirstSearch(int s) traverses vertices reachable from s.
import java.io.*;
import java.util.*;
import java.util.HashMap;

// This class represents a directed graph using adjacency
// list representation
class Graph {
	private int V; // No. of vertices
	private LinkedList<Integer> adj[]; // Adjacency Lists

	// Constructor
	Graph(int v)
	{
		V = v;
		adj = new LinkedList[v];
		for (int i = 0; i < v; ++i)
			adj[i] = new LinkedList<Integer>();
	}

	// Function to add an edge into the graph
	void addEdge(int v, int w) { adj[v].add(w); }

   int[] getReachableNodes(int start, int distance){
      return null;
   }

 	// Driver method to
	public static void main(String args[])
	{
      BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
      try {
          String[] params = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");
          String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

          int start = Integer.parseInt(params[0]);
          int distance = Integer.parseInt(params[1]);

          int n = Integer.parseInt(firstMultipleInput[0]);
          int m = Integer.parseInt(firstMultipleInput[1]);

          Graph graph = new Graph(n);

          List<List<Integer>> edges = new ArrayList<>();

          for (int i = 0; i < m; i++){
              try {
                 String[] edge = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");
                 graph.addEdge(Integer.parseInt(edge[0]), Integer.parseInt(edge[1]));
              } catch (IOException ex) {
                  throw new RuntimeException(ex);
              }
          }
          int[] reachableNodes = graph.getReachableNodes(start, distance);
      } 
      catch (IOException ex) {
          throw new RuntimeException(ex);
      }

	}
}

