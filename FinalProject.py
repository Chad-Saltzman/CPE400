##################################################
######                                      ######
######      CPE 400 Final Project           ######
######          Dana Conley                 ######
######          Ethan Mahoney               ######
######          Chad Saltzman               ######
######          Version 1.0                 ######
######          12/6/2021                   ######
######                                      ######
##################################################

from RoutingProtocol import *
from Graph import *
import sys

#SampleGraph is a baseline graph provided in the Project description         
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

    protocols = ["RIP","OSPF", "Exit"]
    protocol = ""

    print("\t Failed Link/Node Routing Simulation")
    # Continuously loops through the program so simulations of multiple situations can occur
    while True:
        Choice = input("Would you like to use a predefined graph? (Y/N)\n")
        if Choice.upper() == "Y":
            print("The predefined graph is demonstrated below:")
            Network = Graph(sampleGraph)

        elif Choice.upper() == "N":
            Network = Graph()
            user_graph = Network.getGraph()  # Retrieves the user inputted graph from CustomGraph.txt
            Network = Graph(user_graph)  # Creates a new instance of the graph class passing in the user inputted graph.
            print("The inserted graph is demonstrated below")

        else:
            while Choice.upper() != "Y" or Choice.upper() != "N":
                Choice = input("Invalid input\nWould you like to use a predefined graph? Y/N:\n")

        print(Network) # Displays the network graph being used

        FindRoute = RoutingProtocol(Network.graph)

        print("Select a routing protocol to use: ")
        # Loops until a valid option is selected
        while protocol  not in protocols:
            print("1.RIP")
            print("2.OSPF")
            print("3.Exit")
            try:
                protocol = protocols[int(input())-1]  # Assigns the protocol based on the user input
            except:
                print("Invalid input")
                print("Select a routing protocol to use: ")
        if protocol == "Exit":
            sys.exit()  # Exits program if user did not wish to continue
        
        Network.disableNode()  # Prompts user to disable any nodes in the network
        Network.disableLink()  # Prompts user to disable any links in the network
        source, destination = Network.getSourceAndDestinationNodes()  # Prompts the user and returns the source and destination node
        
        if protocol == "RIP": 
            shortest_path = FindRoute.RIP(source = source,destination=destination, nodesOnline=Network.online)  # Calculates and returns the shortest path using the Bellman-Ford algorithm

        elif protocol =="OSPF":
            shortest_path = FindRoute.OSPF(source = source, destination = destination, nodesOnline=Network.online)  # Calculates and returns the shortest path using the Dijkstra algorithm

        print(f"The shortest path from {source} to {destination} is:")
        print(shortest_path)  
        print()
        choice = input("Would you like to run again? (Y/N) ")
        while True:
            if choice.upper() == "Y":
                break 
            elif choice.upper() == "N":
                sys.exit()  # Exits program is user does not want to create a new simulation
            else:
                print("Invalid input")
                choice = input("Would you like to run again? (Y/N) ")


if __name__ == '__main__':
    main() 
