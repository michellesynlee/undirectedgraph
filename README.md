# undirectedgraph
dict/numpy practice

Consider the following undirected graph.
We can represent this graph with the following Python dictionary, often referred to as an adjacency list:
graph = {
"A": ["D", "E"],
"B": ["E", "F"],
"C": ["E"],
"D": ["A", "E"],
"E": ["A", "B", "C", "D"],
"F": ["B"],
"G": []
}
Write a single Python function that takes any such dictionary x as input, for each of the following:
a. Return the number of isolated nodes (i.e. nodes without any connections).
b. Return the number of non-isolated nodes (i.e. nodes with connections).
c. Return the unique edges as a list of tuples (e.g. [("A", "D"), ("A", "E"), ...]). You do not have to worry about the order of tuples in the list.

