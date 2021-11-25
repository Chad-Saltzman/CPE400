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

    def OSPF(self, source, destination, path = []):
        
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
            if node not in path:
                newpath = self.OSPF(node, destination, path)
                if newpath:
                    if not shortest or getCost(newpath) < getCost(shortest):
                        shortest = newpath 
        return shortest