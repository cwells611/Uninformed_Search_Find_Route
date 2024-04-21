import networkx as nx
import sys

#function definitions 
def create_graph(input_file):
    #create new graph to replicate the input city map 
    cities = nx.Graph()
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
   
    #return the created graph 
    return cities


#main()
#open file specified from command line 
input_file = open(sys.argv[1], "r")

#get start and terminal city from command line
start_city = sys.argv[2]
terminal_city = sys.argv[3]

#create the graph with input 
cities = create_graph(input_file)

#check to see if two cities are the same, if so, output and exit
if(start_city == terminal_city):
    print("distance: 0km")
    print("route: ")
    print(start_city + " to " + terminal_city + ", 0km")
    sys.exit(0)
#check to see if either of the cities used in command line are not in input map
if(not cities.has_node(start_city) or not cities.has_node(terminal_city)):
    print("One or both input cities not in input map.")
    sys.exit(1)

#close file
input_file.close()
