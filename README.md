# graph_distance
You are given a directed unweighted graph. Write a function that returns all nodes reachable from a given starting node and using no more than ```distance``` number of edges.

Sample input graph is provided in g1.txt. Input format is
start_node distance
num_nodes num_edges
(list of edges)

Correct answer for g1.txt is provided in g1a.txt

## Java
The function is
```
int [] getReachableNodes(int start, int distance)
```
The function should return an array of nodes reachable from ```start``` and using no more than ```distance``` edges. The ```start``` node should be included in that array.

Open the code in GitHub codespaces, compile and run it with:
```
javac Graph.java
cat g1.txt | java Graph
```
The above command will read the input from g1.txt and execute Graph main method with that input.
## Python
The function is
```
get_reachable_nodes(self, start, distance)
```
The function should return a list containing all the nodes reachable from ```start``` and using no more than ```distance``` edges. The ```start``` node should be included in that list.

Open the code in GitHub codespaces and run it with:
```
cat g1.txt |python graph.py
```
The above command will read the input from g1.txt and execute graph main function with that input.
