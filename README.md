# graph_project
Application to build graphs using the Floyd algorithm and BFS

- In the above code, we first create the graph for which we will use the breadth-first search. Once created, we will create two lists: one to store the visited node of the graph and the other to store the nodes in the queue.
- After the process described above, we will declare a function with parameters as visited nodes, the graph itself and the node respectively. -  And inside the function, we will continue to add the visit and queue lists.
- Then we will run a while loop for the queue of visited nodes and then remove the same node and print it as it is visited.
- Finally, we will run a loop to check for unvisited nodes and then add them from the visited list and the queue list.
- As driver code, we call the user to define a bfs function with the first node we want to visit.
