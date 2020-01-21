"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set() #using set prevents duplicates, O(1) lookup, more space efficient

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.

        if both exist, add a connection from v1 to v2, else raise an error
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex. BFT = Breadth first traversals

        1. create a queue / stack as appropriate
        2. put the starting point in that
        3. while there is stuff in the queue or stack
        4. pop the first item
        5.  if not visited
        6.      do the thing
        7.  then for each edge in the item
        8.      add that edge to the queue or stack
        """
        # 1. create a queue / stack as appropriate
        queue = Queue()
        # 2. put the starting point in that
        queue.enqueue(starting_vertex)
        #make a set to keep track of where we have been
        visited = set()
        # 3. while there is stuff in the queue or stack
        while queue.size() > 0:
        # 4. pop the first item
            vertex = queue.dequeue()
        # 5.  if not visited
            if vertex not in visited:
        # 6.      do the thing
                print(vertex)
        # add to visited:
                visited.add(vertex)
        # 7.  then for each edge in the item
                for next_vert in self.get_neighbors(vertex):

        # 8.      add that edge to the queue or stack
                    queue.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex. DFT = Depth first traversals = USE STACK
        DFT = the minimum spanning trees = minimum spanning forest (haha)



        1. create a queue / stack as appropriate
        2. put the starting point in that
        3. while there is stuff in the queue or stack
        4. pop the first item
        5.  if not visited
        6.      do the thing
        7.  then for each edge in the item
        8.      add that edge to the queue or stack
        """
        # 1. create a queue / stack as appropriate
        stack = Stack()
        # 2. put the starting point in that
        stack.push(starting_vertex)
        #make a set to keep track of where we have been
        visited = set()
        # 3. while there is stuff in the queue or stack
        while stack.size() > 0:
        # 4. pop the first item
            vertex = stack.pop()
        # 5.  if not visited
            if vertex not in visited:
        # 6.      do the thing
                print(vertex)
        # add to visited:
                visited.add(vertex)
        # 7.  then for each edge in the item
                for next_vert in self.get_neighbors(vertex):

        # 8.      add that edge to the queue or stack
                    stack.push(next_vert)

      

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

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
    print("printing graph vertices")
    print(graph.vertices)

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
    print("running bft")
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("running dft")
    graph.dft(1)
    print("running dft recursive")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("running graph.bfs")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("running graph.dfs")
    print(graph.dfs(1, 6))
    print("running graph.dfs_recursive")
    # print(graph.dfs_recursive(1, 6))
