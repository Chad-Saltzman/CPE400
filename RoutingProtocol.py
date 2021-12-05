class RoutingProtocol:
    def __init__(self, graph):
        self.graph = graph 
    
    def RIP(self, source, destination, i, LS, LE, nodesOnline, edgesAvail, path = []):
        path = path + [source]
        if source == destination:
            return path
        shortest = None
        for node in self.graph[source]:
            if node not in path and nodesOnline[node]:
                if LS not in path:
                    newpath = self.RIP(node, destination, i, LS, LE, nodesOnline, edgesAvail, path)
                    if newpath:
                        i = i+1
                        if (not shortest or len(newpath) < len(shortest)) and ((LS, LE) not in path):
                            shortest = newpath

                else:
                    if path[i] != LS and node != LE:
                        newpath = self.RIP(node, destination, i, LS, LE, nodesOnline, edgesAvail, path)
                        if newpath:
                            i = i+1
                            if (not shortest or len(newpath) < len(shortest)) and ((LS, LE) not in path):
                                shortest = newpath
                    else:
                        newpath = self.RIP(node, destination, i, LS, LE, nodesOnline, edgesAvail, path)
        return shortest

    def OSPF(self, source, destination, j, LS, LE, nodesOnline, edgesAvail, path = []):
        
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
                if LS not in path:
                    #if node == LE:
                    newpath = self.RIP(node, destination, j, LS, LE, nodesOnline, edgesAvail, path)
                    if newpath:
                        j = j+1
                        if (not shortest or len(newpath) < len(shortest)) and ((LS, LE) not in path):
                            shortest = newpath

                else:
                    if path[j] != LS and node != LE:
                        newpath = self.RIP(node, destination, j, LS, LE, nodesOnline, edgesAvail, path)
                        if newpath:
                            j = j+1
                            if (not shortest or len(newpath) < len(shortest)) and ((LS, LE) not in path):
                                shortest = newpath
                    else:
                        newpath = self.RIP(node, destination, j, LS, LE, nodesOnline, edgesAvail, path)
        return shortest
