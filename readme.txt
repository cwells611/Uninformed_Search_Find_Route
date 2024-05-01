Caden Wells 10888879 
Python 3.9.7
Microsoft Windows 11 10.0.22631

My code is broken up into two main sections. The first contains various functions needed to prep the input, 
preform the search, and other various smaller functionalities that I needed. The second second section 
is where the command line arguments are read in, edge cases are handled, and the functions are called
in the order which they are needed. There are two main functions, create_graph() and find_shortest_path(). 
The first function takes in the input file and creates a networkx undirected graph with all of the cities 
and paths between the cities that are found in the input file. There is some pre-processing that is done on the 
lines that are read in such as removing whitespace and spliting each line into the two cities and the weight. 
After this, each city is added to the graph and the edges with their weights are added as well. The graph 
is returned from this function. The search function applies the uniform cost search algorithm on the graph 
with the given start and end cities. This algorithm uses a priority queue to keep track of the fringe nodes that
have not been expanded. The search uses a BFS approach were all of the neighbors adjacent to the node being expanded
are added to the priority queue. As you go deeper, the weight of each node is updated with the total path weight
from the root node to the current node being looked at. Once the goal node has been chosen from the fringe for expansion, 
the algorithm breaks, and then reconstructs the path taken by using the parent attribute of each node. Once the path has 
been properly reconstructed, the output is produced. 

In order to run this code you need three libraries; sys, networkx, and queue. To install these, use the pip
command on your terminal. 
pip install networkx
pip install sys
pip install queue 
As this project was written in python, there is not complier needed and it can be run directly from the terminal. 
There need to be 4 arguments given in the command line, the file name, the input text file, the start city, and the 
end city. Here is an example of how to run it using the given input1.txt file:
python .\find_route.py .\input1.txt Bremen Frankfurt
From there the output will be written from the console. 