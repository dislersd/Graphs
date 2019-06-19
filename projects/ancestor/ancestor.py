'''
Vertices = Integers
Edges = Connections from parent to children

1. take all numbers and turn into vertices
2. create edges for children to parent vertices
3. dft and find longest path
4. Path with longest length, last element should be the oldest ancestor
'''

from util import Stack, Queue

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def oldest_ancestor(self, starting_vertex, data_set):
        for num in data_set:
            self.add_vertex(num)
        # this assumes the data set is a list
        # every two elements get an edge with parent to child relationship
        # [1,3,2,5] => {1: no parent, 3: 1, 2: no parent, 5: 2}    
        for i in range(1, len(data_set), 2):
            self.add_edge(data_set[i], data_set[i - 1])
        # if input idividual has no parent return -1    
        if self.vertices[starting_vertex] == set():
            return -1
        stack = Stack()
        stack.push([starting_vertex])
        oldest = []
        while stack.size() > 0:
            path = stack.pop()
            vertex = path[-1]
            if len(path) > len(oldest):
                oldest = path
            if len(path) == len(oldest) and path[-1] < oldest[-1]:
                oldest = path
            for neighbor in self.vertices[vertex]:
                new_path = path.copy()
                new_path.append(neighbor)
                stack.push(new_path)

        return oldest[-1]

x = Graph()
print(x.oldest_ancestor(6, [1,3,2,3,3,6,5,6,5,7,4,5,4,8,8,9,11,8,10,1]))
# print(x.vertices)