'''
Vertices = Integers
Edges = Connections from parent to children

1. take all numbers and turn into vertices
2. create edges for children to parent vertices
3. dft and find longest path
4. Path with longest length, last element should be the oldest ancestor
'''

from util import Stack, Queue

from collections import deque


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)


def earliest_ancestor(data_set, starting_vertex):
    graph = Graph()
    for pair in data_set:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        graph.add_edge(pair[1], pair[0])
    print(graph.vertices)

    if graph.vertices[starting_vertex] == set():
        return -1
    breakpoint()
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
        for neighbor in graph.vertices[vertex]:
            new_path = path.copy()
            new_path.append(neighbor)
            stack.push(new_path)

    return oldest[-1]


# x = Graph()

data_set = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1), (20, 4), (25, 20)]
# for pair in data_set:
#     x.add_vertex(pair[0])
#     x.add_vertex(pair[1])
#     x.add_edge(pair[0], pair[1])
# print(x.vertices)


{
  1: {3},
  3: {}
}

# [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(data_set, 6))
