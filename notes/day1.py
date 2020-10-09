"""
Adjacency list 
dictionary with sets of neiboring vertices
for the  add_edge method, wouldn't this line:

    ` self.vertices[v1] = v2 `
replace the empty set with an instance of v2 instead of adding to the set?

Graphs
------
Nodes (also called "verts", "vertexes", "vertices") are connected by edges

Edges _may_ have numeric weights associated with them
* If not shown, assume all weights are 1 ("unweighted graph")
Edges can be directed (one way) or undirected (two way)
* If there are _only_ undirected edges, we call it an "undirected graph"
* Else we call it a "directed graph"

Cycle: we can traverse and get back to the starting node somehow
* If a graph has any cycles in it, we call it a "cyclic graph".
* Else it's an "acyclic graph".

Representation of graphs
------------------------
Which nodes are adjacent ("directly connected") to a particular node.
Adjacency matrix
* Big grid that has true/false values showing which nodes are adjacent
  * Or edge weights
Adjacency list (what we'll use)
A: {B, D}
B: {D, C}
C: {C, B}
D: {}

BFT
---
Init:
    Add the starting vert to the queue
While the queue is not empty:
    Pop current vert off queue
    If not visited:
        "Visit" the node
        Track it as visited
        Add all its neighbors (adjacent nodes) to the queue


"""
from collections import deque

class Graph:

    def __init__(self):
        # Graph class has a property vertices
        self.vertices = {} # keys are all verts, values are sets of adj verts

    def __repr__(self):
        return str(self.vertices)

    # to add a graph vertex pass in the value of vertex
    def add_vertex(self, vertex_id):
        # IF vertex does not exist in the graph vertices
        if vertex_id not in self.vertices:
            # assign it as a key in self.vertices and set the value to a new set
            self.vertices[vertex_id] = set()

    # to connect nodes with an edge pass in both nodes
    def add_edge(self, v1, v2):
        # check both vertices exist 
        if v1 in self.vertices and v2 in self.vertices:
            # then add to nodes adj verts
            self.vertices[v1].add(v2)
    
    def is_connected(self, v_from, v_to):
        # check if they both exist in the graph
        if v_from in self.vertices and v_to in self.vertices:
            # return true or false value
            return v_to in self.vertices[v_from]
        else:
            # if vert does not exist return error msg because None return types can break search algos
            raise IndexError("nonexistent vertex")
    


    def get_neighbors(self, vertex_id):
        # simply return the values paired to that vert 
        return self.vertices[vertex_id] if vertex_id in self.vertices else set()

    def dft(self, starting_vertex):
        stack = deque() ## alternatively we could import the stack from utils.py and just use pop() instead of popleft() 
        visited = set()

        # Init:
        stack.append(starting_vertex)

        # while stack is not empty
        while len(stack) > 0:

            currNode = stack.pop() 

            if currNode not in visited:
                print(currNode) # "visit" node

                visited.add(currNode)
                for neighbor in self.get_neighbors(currNode):
                    stack.append(neighbor)

    def bft(self, starting_vertex):
        visited = set()
        queue = deque() ## alternatively we could import the stack from utils.py and just use pop() instead of popleft() 
        
        #  Init:
        queue.append(starting_vertex)

        # while queue isn't empty
        while len(queue) > 0:
            
            currNode = queue.popleft() ## built in method from collections deque 

            if currNode not in visited:
                print(currNode) # alternatively "visit" node here 

                visited.add(currNode)

                for neighbor in self.get_neighbors(currNode):
                    queue.append(neighbor)

    # Returns path from starting vertex to destination vertex
    def dfs(self, starting_vertex, destination_vertex):
        stack = deque()
        # Each element in the stack is the current path e.g [1, 2, 3..]
        stack.append([starting_vertex])
        visited = set()
        while len(stack) > 0:
            currPath = stack.pop() # [1, 2, 3]
            currNode = currPath[-1] # 3
            if currNode == destination_vertex:
                return currPath
            if currNode not in visited:
                visited.add(currNode)
                for neighbor in self.get_neighbors(currNode):
                    newPath = list(currPath)
                    newPath.append(neighbor)
                    stack.append(newPath)

g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)

g.add_edge(2, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
print("graph vertices ")
print(g.vertices)
print("breadth first traveral")
g.bft(1)
print("depth first traversal")
g.dft(1)