import re 
import copy

class Graph:

    def __init__(self, graphdict = {}):
        self.graph = copy.deepcopy(graphdict)
        self.edges = self.generate_edges()
        self.online = {}

        if graphdict:
            for node in self.graph:
                self.online[node] = True
            
    def generate_edges(self):
        edges = []

        for node in self.graph:
            for neighbour in self.graph[node]:
                if neighbour:
                    edges.append((node, neighbour))
        return edges 
    
    def __str__(self):
        output = ""
        for node in self.graph:
            Connections = node + " -> "
            for neighbor in self.graph[node]:
                Connections = Connections + neighbor + " -> "
            output = output + '\n' + Connections.strip().strip('->')
        return output.lstrip('\n')

    def getGraph(self):
        with open ("CustomGraph.txt", "r") as graphFile:
            currentNode = ""
            fileInput = graphFile.readlines()
            for line in fileInput:
                line = line.strip('\n')
                line = line.split(",")
                currentNode = line[0]
                self.graph[currentNode] = {}
                self.online[currentNode] = True
                for node in line:
                    if node == currentNode:
                        continue
                    node = re.split(r'\((?P<cost>\d+)\)', node)
                    if len(node) == 3:
                        del node[2]
                    if len(node) == 2:
                        self.graph[currentNode][node[0]] = int(node[1])
                    else:
                        self.graph[currentNode][node[0]] = 1

    def getNodes(self):
        nodes = []
        for node in self.graph:
            nodes.append(node)
            
        return nodes

    def isOnline(self, node):
        return self.online[node]

    def disableLink(self):
        choice = input("Would you like to disable a link? (Y/N)")

        while True:
            if choice.upper() == 'Y':
                node1 = input(f"select the starting node that the link is connected to\n{self.getNodes()}\n").upper()
                node2 = input(f"select the ending node that the link is connected to\n{self.getNodes()} \n").upper()
                self.graph[node1].pop(node2.upper(),"Link does not exist")
                link_exists = self.graph[node2].pop(node1.upper(),"Link does not exist")
                if link_exists == "Link does not exist":
                    print(link_exists)
                    continue 
                print(f"The link from {node1} to {node2} is now offline")
                choice = input("Would you like to disable another link? (Y/N)\n")
            elif choice.upper() == "N":
                    break 
            else:
                print("Invalid input")
                choice = input("Would you like to disable a node? (Y/N)\n")

    def disableNode(self):
        choice = input("Would you like to disable a node? (Y/N)\n")

        while True:
            if choice.upper() == 'Y':
                node = input(f"Select a node to be disabled\n{self.getNodes()}\n").upper()
                self.online[node] = False
                print(f"node {node} is now offline")
                choice = input("Would you like to disable another node? (Y/N)\n")
            elif choice.upper() == 'N':
                break
            else:
                print("Invalid input")
                choice = input("Would you like to disable a node? (Y/N)\n")

    def getSourceAndDestinationNodes(self):
        nodes = self.getNodes()
        source = ""
        destination = ""

        source = input(f"Select the source node from the following\n{self.getNodes()}\n").upper()
        while source not in nodes:
            
            if source not in nodes or not self.isOnline(source):
                source = ""
                print("Invalid input or current node is offline")
                source = input(f"Select the source node from the following:\n{self.getNodes()}\n").upper()

        destination = input(f"\nSelect the destination node from the following:\n{self.getNodes()}\n").upper()

        while destination not in nodes:
            if destination not in nodes or not self.isOnline(destination):
                destination = ""
                print("Invalid input or current node is offline")
                destination = input(f"Select the destination node from the following:\n{self.getNodes()}\n").upper()

        return source, destination