

class RoutingProtocol:
    def __init__(self, graph):
        self.graph = graph 
    
    def RIP(self, source, destination, path = []):
        path = path + [source]
        if source == destination:
            return path
        shortest = None
        for node in self.graph[source]:
            if node not in path:
                newpath = self.RIP(node, destination, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

    def OSPF(self, source, destination):
        pass 


        

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
        userinput = ""
        print("Enter in your graph in the following structure: <node>,<Connected to 1>, <Connected to 2> ... <Enter>")
        print("When you have completed entering all the nodes and connections, type done and press enter")
        currentNode = ""  
        while currentNode != "done":
            userinput = input()
            userinput = userinput.split(",")
            currentNode = userinput[0]
            self.graph[userinput[0]] = []
            
            userinput.pop(0)
            for node in userinput:
                self.graph[currentNode].append(node)
        del self.graph["done"]

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
        

            

        

sampleGraph = {
    'A':['B'],
    'B':['A','C','D'],
    'C':['B','E'],
    'D':['B','E','F','G'],
    'E':['C','D','H'],
    'F':['D','I','J'],
    'G':['D','J'],
    'H':['E'],
    'I':['F','K'],
    'J':['G','F'],
    'K':['I','L','M'],
    'L':['K','M','N','O','P'],
    'M':['K','L','P'],
    'N':['L','O'],
    'O':['L','N','P'],
    'P':['L','M','O'],
}



def main():

    protocols = ["RIP","OSPF"]
    protocol = ""

    print("\t Failed Link/Node Routing Simulation")

    Choice = input("Would you like to use a predefined graph? Y/N: ")
    if Choice.upper() == "Y":
        print("The predefined graph is demonstrated below:")
        Network = Graph(sampleGraph)

    elif Choice.upper() == "N":
        Network = Graph()
        Network.getGraph()
        print("The inserted graph is demonstrated below")

    else:
        while Choice.upper != "Y" or Choice.upper != "N":
            Choice = input("Invalid input\nWould you like to use a predefined graph? Y/N: ")

    print(Network)

    FindRoute = RoutingProtocol(Network.graph)

    print("Select a routing protocol to use: ")
    while protocol  != "RIP" and protocol != "OSPF":
        print("1.RIP")
        print("2.OSPF")
        try:
            protocol = protocols[int(input())-1]
        except:
            print("Invalid input")
            print("Select a routing protocol to use: ")

    source, destination = Network.getSourceAndDestinationNodes()
    if protocol == "RIP": 
        shortest_path = FindRoute.RIP(source = source,destination=destination)

    elif protocol =="OSPF":
        shortest_path = FindRoute.OSPF(source = source, destination = destination)
    print(f"The shortest path from {source} to {destination} is:")
    print(shortest_path)


if __name__ == '__main__':
    main()
