"""
RoutingProtocol.py
Version 1.0 
12/6/2021

The RoutingProtocol.py file contains the RoutingProtocol
class which contains functions for the routing protocols 
RIP and OSPF.

The RIP Routing protocol uses the bellman-ford algorithm 
which determines the path based on hop count. The OSPF 
algorithm uses dijkstra algorithm which determines the 
path based on the value of each link.

"""


class RoutingProtocol:

    def __init__(self, graph):
        self.graph = graph 
    
    # Calculates and returns the shortest path using the bellman-ford algorithm
    def RIP(self, source, destination, nodesOnline, path = []):
        path = path + [source]
        if source == destination:  # returns the source node if source and destination nodes are the same
            return path
        shortest = None
        for node in self.graph[source]:
            if node not in path and nodesOnline[node]:
                newpath = self.RIP(node, destination, nodesOnline, path)  # Recursively calls RIP to create every possible path in the network
                if newpath:
                    if not shortest or len(newpath) < len(shortest):  # Checks to see if the latest path is shorter than the previously shortest path
                        shortest = newpath  
        return shortest

    # Calculates and returns the shortest path using the dijkstra algorithm
    def OSPF(self, source, destination, nodesOnline, path = []):
        
        # Calculates the cost value for a specific path based on the cost of each link on the path.
        def getCost(newPath):
            cost = 0
            for i in range(len(newPath)):
                for neighbor in self.graph[newPath[i]]:
                    if len(newPath) >= i+2 and neighbor == newPath[i+1]:
                        cost = cost + self.graph[newPath[i]][neighbor]
                        break
            return cost
        
        path = path + [source]
        if source == destination:
            return path 
        shortest = None 
        for node in self.graph[source]:
            if node not in path and nodesOnline[node]:
                newpath = self.OSPF(node, destination, nodesOnline, path)  # Recursively calls OSPF to create every possible path in the network
                if newpath:
                    if not shortest or getCost(newpath) < getCost(shortest):  # Checks to see if the latest path is shorter than the previously shortest path based on the total cost
                        shortest = newpath 
        return shortest