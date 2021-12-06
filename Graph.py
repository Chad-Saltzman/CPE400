"""
Graph.py 
Version 1.0 
12/6/2021

The Graph.py file contains the graph class which is used to 
construct, manipulate, and gather information from a graph.

"""



import re 
import copy

class Graph:

    def __init__(self, graphdict = {}):
        self.graph = copy.deepcopy(graphdict)  # Creates a deep copy of the graph so that the original graph is not manipulated
        self.edges = self.generate_edges()
        self.online = {}

        if graphdict:
            for node in self.graph:
                self.online[node] = True

    # Determines the different edges within the graph and returns a list of every edge        
    def generate_edges(self):
        edges = []

        for node in self.graph:
            for neighbour in self.graph[node]:
                if neighbour:
                    edges.append((node, neighbour))
        return edges 
    
    # Cleanly displays the graph to the user
    def __str__(self):
        output = ""
        for node in self.graph:
            Connections = node + " -> "
            for neighbor in self.graph[node]:
                Connections = Connections + neighbor + " -> "
            output = output + '\n' + Connections.strip().strip('->')  # Removes the trailing -> from the graph output
        return output.lstrip('\n')  # returns the graph output but removes any preceeding extra lines

    # Reads in a graph from the CustomGraph.txt file and stores it 
    def getGraph(self):
        with open ("CustomGraph.txt", "r") as graphFile:  # Opens CustomGraph.txt file
            currentNode = ""
            fileInput = graphFile.readlines()  # Reads every line of the file
            for line in fileInput:
                line = line.strip('\n')  # Removes any newline characters
                line = line.split(",")  # Converts the line into a list with each node as an entry
                currentNode = line[0]
                self.graph[currentNode] = {}
                self.online[currentNode] = True
                for node in line:
                    if node == currentNode:  # Skips the root node
                        continue
                    node = re.split(r'\((?P<cost>\d+)\)', node)  # Seperates the node from the link cost value
                    if len(node) == 3:
                        del node[2]  # Removes extra comma if one exists
                    if len(node) == 2:
                        self.graph[currentNode][node[0]] = int(node[1])  # Adds a new dictionary to the graph dictionary with node as a key and the cost as the value
                    else:
                        self.graph[currentNode][node[0]] = 1  # If no cost value exists then it defaults to 1
        return self.graph

    # Returns a list of all nodes present in the graph
    def getNodes(self):
        nodes = []
        for node in self.graph:
            nodes.append(node)
            
        return nodes

    # Returns the online status of a node
    def isOnline(self, node):
        return self.online[node]

    # Manipulates the graph so that a link no longer exists
    def disableLink(self):
        choice = input("Would you like to disable a link? (Y/N)")

        # Loops until the user no longer wants to disable any links
        while True:
            if choice.upper() == 'Y':
                node1 = input(f"select the starting node that the link is connected to\n{self.getNodes()}\n").upper()
                node2 = input(f"select the ending node that the link is connected to\n{self.getNodes()} \n").upper()
                self.graph[node1].pop(node2.upper(),"Link does not exist")  # Removes the connection from the first node to the second node in the graph
                link_exists = self.graph[node2].pop(node1.upper(),"Link does not exist")  # Removes the connection from the second node to the first node in the graph

                if link_exists == "Link does not exist":  # Checks if the link requested by the user did not originally exist
                    print(link_exists)
                    continue 
                print(f"The link from {node1} to {node2} is now offline")
                choice = input("Would you like to disable another link? (Y/N)\n")
            elif choice.upper() == "N":
                    break 
            else:
                print("Invalid input")
                choice = input("Would you like to disable a node? (Y/N)\n")

    # Manipulates the graph so that a node is no longer active
    def disableNode(self):
        choice = input("Would you like to disable a node? (Y/N)\n")

        # Loops until the user no longer wants to disable any nodes
        while True:
            if choice.upper() == 'Y':
                node = input(f"Select a node to be disabled\n{self.getNodes()}\n").upper()
                self.online[node] = False  # Sets the node to offline
                print(f"node {node} is now offline")
                choice = input("Would you like to disable another node? (Y/N)\n")
            elif choice.upper() == 'N':
                break
            else:
                print("Invalid input")
                choice = input("Would you like to disable a node? (Y/N)\n")

    # Gets input from the user as to what the source and destination node is of the path
    def getSourceAndDestinationNodes(self):
        nodes = self.getNodes()
        source = ""
        destination = ""

        source = input(f"Select the source node from the following\n{self.getNodes()}\n").upper()
        
        # Loops until the user selects an available node
        while source not in nodes or not self.isOnline(source):
            source = ""
            print("Invalid input or current node is offline")
            source = input(f"Select the source node from the following:\n{self.getNodes()}\n").upper()

        destination = input(f"\nSelect the destination node from the following:\n{self.getNodes()}\n").upper()

        # Loops until the user selects an available destination node
        while destination not in nodes or not self.isOnline(destination):
            destination = ""
            print("Invalid input or current node is offline")
            destination = input(f"Select the destination node from the following:\n{self.getNodes()}\n").upper()

        return source, destination