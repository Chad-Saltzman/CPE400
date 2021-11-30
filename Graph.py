import re 

class Graph:

    def __init__(self, graphdict = {}):
        self.graph = graphdict 
        self.edges = self.generate_edges()
        self.online = {}

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

    def disableNode(self):
        choice = input("Would you like to disable a node? (Y/N) ")

        while True:
            if choice.upper() == 'Y':
                node = input("Select a node to be disabled: ")
                self.online[node] = False
                break
            elif choice.upper() == 'N':
                break
            else:
                print("Invalid input")
                choice = input("Would you like to disable a node? (Y/N) ")

    def getSourceAndDestinationNodes(self):
        nodes = self.getNodes()
        source = ""
        destination = ""
        print("Select the source node from the following: ")

        while source not in nodes:
            print(nodes)
            source = input()
            if source not in nodes or not self.isOnline(source):
                source = ""
                print("Invalid input or current node is offline")
                print("Select the source node from the following: ")

        print("\nSelect the destination node from the following: ")

        while destination not in nodes:
            print(nodes)
            destination = input()
            if destination not in nodes or not self.isOnline(destination):
                destination = ""
                print("Invalid input or current node is offline")
                print("Select the destination node from the following: ")

        return source, destination