import networkx as nx
import queue
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
        #if neither of the cities are already in the graph, add them 
        if(not cities.has_node(input_array[i][0])):
            cities.add_node(input_array[i][0], parent='')
        if(not cities.has_node(input_array[i][1])):
            cities.add_node(input_array[i][1], parent='')
        cities.add_edge(input_array[i][0], input_array[i][1], weight=int(input_array[i][2]))
   
    #return the created graph 
    return cities

#compares current city with goal to determine when to terminate search
def is_goal_node(goal_city, current_city):
    if(current_city == goal_city):
        return True
    return False

#function to get the neighbors of a node (next level down in graph)
#also gets the edge weight between root and each neighbor
def get_neighbors(root, graph: nx.Graph):
    neighbors = []
    root_neighbors = graph.neighbors(root)
    for neighbor in root_neighbors:
        weight = graph.get_edge_data(root, neighbor)
        weight = int(weight['weight'])
        neighbor_pair = [neighbor, weight]
        neighbors.append(neighbor_pair)
    return neighbors
    

def find_shortest_path(start, end, map: nx.Graph):
    #at the start of the search, set start city's parent to itself 
    map.nodes[start]['parent'] = start
    #queue to hold the fringe nodes while searching
    fringe = queue.PriorityQueue()     
    #intially populate the fringe with first level of neighbors 
    next_level = get_neighbors(start, map)
    for i in range(len(next_level)):
        #set the parent of the node to the root node initially 
        map.nodes[next_level[i][0]]['parent'] = start
        #put each neighbor into the priority queue based on length 
        fringe.put((next_level[i][1], next_level[i][0]))
    while(True):
        #pull top node out of fringe for expansion 
        expanded_node = fringe.get()
        expanded_city = expanded_node[1]
        #after top node has been selected, get its neighbors 
        next_level = get_neighbors(expanded_city, map)
        #add nodes to fringe, but with total path weight 
        for i in range(len(next_level)):
            #set the parent of each node we are putting into the fringe as the node being expanded 
            if map.nodes[next_level[i][0]]['parent'] == '':
                map.nodes[next_level[i][0]]['parent'] = expanded_city
            #put into fringe, but instead of just path weight, its path weight + weight of expanded node 
            fringe.put((next_level[i][1] + expanded_node[0], next_level[i][0]))
        #check to see if the node we are going to expand is the goal node 
        if(is_goal_node(end, expanded_node[1])):
            #print distance of path
            print("distance: " + str(expanded_node[0]) + " km")
            break
    print(nx.shortest_path(map, start, end, weight='weight'))
    

    #once out of the for loop we need to reconstruct the path working up through parent nodes
    path = [end]
    while (not end == start):
        end = map.nodes[end]['parent']
        path.append(end)
    #reverse the path to go from start to end
    path.reverse()
    #output route taken
    print("route:")
    for i in range(len(path) - 1):
        print(path[i] + " to " + path[i+1] + ", " + str(map.edges[path[i], path[i+1]]['weight']) + " km")    
    
        


#main()
#check to see if the right number of arguments is presented 
if(not len(sys.argv) == 4):
    print("Please provide 3 arguments: input file, start city, end city")
    sys.exit(1)

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

#check to see if no route exists between the two input cities 
if(not nx.has_path(cities, start_city, terminal_city)):
    print("distance: infinity")
    print("route:")
    print("none")
    sys.exit(0)

find_shortest_path(start_city, terminal_city, cities)

#close file
input_file.close()
