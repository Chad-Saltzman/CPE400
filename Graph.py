import re 

class Graph:

    def __init__(self, graphdict = {}):
        self.graph = graphdict 
        self.edges = self.generate_edges()

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

    def getSourceAndDestinationNodes(self):
        nodes = self.getNodes()
        source = ""
        destination = ""
        print("Select the source node from the following: ")

        while source not in nodes:
            print(nodes)
            source = input()
            if source not in nodes:
                print("Invalid input")
                print("Select the source node from the following: ")

        print("\nSelect the destination node from the following: ")

        while destination not in nodes:
            print(nodes)
            destination = input()
            if destination not in nodes:
                print("Invalid input")
                print("Select the destination node from the following: ")

        return source, destination