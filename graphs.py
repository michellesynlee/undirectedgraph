import numpy as np
#a function that takes a dictionary as input for...a, b, c
graph = {
    "A": ["D", "E"],
    "B": ["E", "F"],
    "C": ["E"],
    "D": ["A", "E"],
    "E": ["A", "B", "C", "D"],
    "F": ["B"],
    "G": []
}
def undirectedGraphStuff(graph):
    for key, value in graph.items():
        if not value: #part a: nodes without any connections, aka keys with no values
            print("part a: ")
            print(key)
        if value:
            print("part b: ")
            print(key) #part b: nodes with non-isolated nodes, aka keys with values

    print("part c: ") #part c: unique edges as a list of tuples
    for key, item in graph.items():
        for value in item:
            print(key, "+", value)

    #part d: 2D numpy adjacency matrix
    arr = np.zeros((7,7))
    alphaDict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}

    for key, item in graph.items():
        for value in item:
            print(key, "+", value)
            arr[alphaDict.get(key)][alphaDict.get(value)] = 1

    print(arr)

undirectedGraphStuff(graph)
