"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """

        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        
        # create an empty ser to store visited nodes
        visited = set()
        # create an empty que
        q = Queue()
        q.enqueue(starting_vertex)
        # while the queue is not empty...
        while q.size() > 0:
            # Deque the first vertex
            v = q.dequeue()
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                # Then add all of its neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)

# visited = {1, 2, 3, 4, 5}
# queue = [5, 7, 6]
# print: 1, 2, 3

# v = 4

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        
        # create an empty ser to store visited nodes
        visited = set()
        # create an empty que
        s = Stack()
        s.push(starting_vertex)
        # while the queue is not empty...
        while s.size() > 0:
            # Deque the first vertex
            v = s.pop()
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                # Then add all of its neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """

        if visited is None:
            visited = set()
        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
            for neighbor in self.vertices[starting_vertex]:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        
        # create an empty set to store visited nodes
        visited = set()
        # create an empty que and enque A PATH to the starting vertex
        q = Queue() # []
        q.enqueue([starting_vertex]) # [ [1] ]
        # while the queue is not empty...
        while q.size() > 0:
            # Deque the first PATH
            path = q.dequeue()
            # GRAB THE VERTEX FROM THE END OF THE PATH
            vertex = path[-1]
            # IF VERTEX = TARGET, RETURN PATH
            if vertex == destination_vertex:
                return path
            # If that vertex has not been visited...
            if vertex not in visited:
                # Mark it as visited
                visited.add(vertex)
                # Then add A PATH TO all of its neighbors to the back of the que
                for neighbor in self.vertices[vertex]:
                # Copy the path
                    new_path = path.copy()
                    # other way to copy
                    # new_path = list(path) or new_path = path + [neighbor]
                    # Append the nieghbor to the back of the copy
                    new_path.append(neighbor)
                    #Enque the copy
                    q.enqueue(new_path)
        return None


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        
        # Create empty stack and push A PATH to the starting vertex ID
        stack = Stack()
        stack.push([starting_vertex])
        # create a set to store visited
        visited = set()
        # while stack is not empty
        while stack.size() > 0:
            # pop first path
            path = stack.pop()
            # grab last vertex from the path
            vertex = path[-1]
            # if vertex is target, return path
            if vertex == destination_vertex:
                return path
            # if vertex not visited add to visited set
            if vertex not in visited:
                visited.add(vertex)
            # then add PATH to neigbors
                for neighbor in self.vertices[vertex]:
                    new_path = path.copy()
                    new_path.append(neighbor)
                    if new_path[-1] == destination_vertex:
                        path = new_path
                        return path
                    else:
                        stack.push(new_path)
                        
        return None





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 5))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 3))

