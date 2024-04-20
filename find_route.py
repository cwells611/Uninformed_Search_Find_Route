import networkx as nx
import sys

#create new graph to replicate the input city map 
cities = nx.Graph()

#open file specified from command line 
input_file = open(sys.argv[1], "r")

#create list of lists where each sub list contains the elements of a line of the input
input_lines = input_file.readlines(); 
input_array = []
for line in input_lines:
    line = line.strip()
    #check for end of input 
    if line == "END OF INPUT":
        break; 
    individual_line = []
    elements = line.split()
    for element in elements:
        individual_line.append(element)
    input_array.append(individual_line)

#loop through the list of lists and add nodes, edges, 
#and weights to city graph 
for i in range(len(input_array)):
    cities.add_node(input_array[i][0])
    cities.add_node(input_array[i][1])
    cities.add_edge(input_array[i][0], input_array[i][1], weight=input_array[i][2])



#close file
input_file.close()
