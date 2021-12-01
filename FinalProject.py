

from RoutingProtocol import *
from Graph import *
        
sampleGraph = {
    'A':{'B':5},
    'B':{'A':5,'C':4,'D':2},
    'C':{'B':4,'E':2},
    'D':{'B':2,'E':5,'F':1,'G':4},
    'E':{'C':2,'D':5,'H':5},
    'F':{'D':1,'I':1,'J':3},
    'G':{'D':4,'J':5},
    'H':{'E':5},
    'I':{'F':1,'K':2},
    'J':{'G':5,'F':3},
    'K':{'I':2,'L':1,'M':4},
    'L':{'K':1,'M':2,'N':4,'O':1,'P':5},
    'M':{'K':4,'L':2,'P':2},
    'N':{'L':4,'O':2},
    'O':{'L':1,'N':2,'P':3},
    'P':{'L':5,'M':2,'O':3},
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
        while Choice.upper() != "Y" or Choice.upper() != "N":
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

    Network.disableNode()
    Network.disableLink()
    source, destination = Network.getSourceAndDestinationNodes()
    if protocol == "RIP": 
        shortest_path = FindRoute.RIP(source = source,destination=destination, nodesOnline=Network.online)

    elif protocol =="OSPF":
        shortest_path = FindRoute.OSPF(source = source, destination = destination, nodesOnline=Network.online)
    print(f"The shortest path from {source} to {destination} is:")
    print(shortest_path)

if __name__ == '__main__':
    main()
