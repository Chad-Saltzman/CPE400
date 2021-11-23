




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
def generate_edges(graph):
    edges = []

    for node in graph:
        for neighbour in graph[node]:
            if neighbour:
                edges.append((node, neighbour))
    return edges 




print("\t Failed Link/Node Routing Simulation")

useSampleGraph = True 
Choice = input("Would you like to use a predefined graph? Y/N: ")
if Choice.upper() == "Y":
    
    print("The predefined graph is demonstrated below:")
    for node in sampleGraph:
        output = node + " -> "
        for neighbor in sampleGraph[node]:
            output = output + neighbor + " -> "
        print(output.strip().strip('->'))
        output = ""