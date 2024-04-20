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


#loop through the input file and add nodes, edges, 
#and weights to city graph 


#close file
input_file.close()
