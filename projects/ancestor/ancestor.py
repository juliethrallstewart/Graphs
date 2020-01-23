from util import Stack, Queue
from graph import Graph


#Queue is Breath First.. and provides the shortest path but doesnt build a tree because it jumps around
# unlike Depth first which takes longer but builds a tree

# print graph.vertices

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        #build edges in reverse
        graph.add_edge(pair[1], pair[0])
        print(f"pair[1] {pair[1]}, pair[0] {pair[0]}")
    #do a BFS (storing the path)
    q = Queue()
    q.enqueue([starting_node])
    max_path_len = 1
    earliest_ancestor = -1
    while q.size() > 0:
        print(q.size(), "Q.SIZE")
        path = q.dequeue()
        print(path, "PATH")
        v = path[-1]
        print(v, "V")
        print(f"len(path) {len(path)} >= max_path_len {max_path_len} and v {v} < earliest_ancestor {earliest_ancestor}) or (len(path) {len(path)} > max_path_len {max_path_len}")
        if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
            earliest_ancestor = v
            print(earliest_ancestor, "EARLIEST ANCESTOR")
            max_path_len = len(path)
            print(max_path_len, 'MAX PATH LEN')
        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            print(path_copy, "PATH COPY")
            path_copy.append(neighbor)
            print(neighbor, "APPENDED NEIGHBOR")
            q.enqueue(path_copy)
    return earliest_ancestor

    
 


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 1)) #10
print(earliest_ancestor(test_ancestors, 2)) # -1
print(earliest_ancestor(test_ancestors, 3)) #10
print(earliest_ancestor(test_ancestors, 4)) # -1
print(earliest_ancestor(test_ancestors, 5)) #4
print(earliest_ancestor(test_ancestors, 6)) #10
print(earliest_ancestor(test_ancestors, 7)) #4
print(earliest_ancestor(test_ancestors, 8)) #4
print(earliest_ancestor(test_ancestors, 9)) #4
print(earliest_ancestor(test_ancestors, 10)) # -1
print(earliest_ancestor(test_ancestors, 11)) # -1

    #    queue = Queue()
    #     # Put the starting point in that
    #     # Enstack a list to use as our path
    #     queue.enqueue([starting_vertex])
    #     # Make a set to keep track of where we've been
    #     visited = set()
    #     # While there is stuff in the queue/stack
    #     while queue.size() > 0:
    #     #    Pop the first item
    #         path = queue.dequeue()
    #         vertex = path[-1]
    #     #    If not visited
    #         if vertex not in visited:
    #             if vertex == destination_vertex:
    #                 # Do the thing!
    #                 return path
    #             visited.add(vertex)
    #     #       For each edge in the item
    #             for next_vert in self.get_neighbors(vertex):
    #             # Copy path to avoid pass by reference bug
    #                 new_path = list(path) # Make a copy of path rather than reference
    #                 new_path.append(next_vert)
    #                 queue.enqueue(new_path)

    # def earliest_ancestor(ancestors, starting_node):
    #     # Create a queue/stack as appropriate
    # result = []
    # queue = Queue()
    # # Put the starting point in that
    # # Enstack a list to use as our path
    # for ancestor in ancestors:
    #     # print(ancestor)
    #     queue.enqueue(ancestor)
    #     # Make a set to keep track of where we've been
    #     # for item in stack.stack:
    #     #     print(item, "ITEM IN STACK")
    #     # print(len(stack.stack), "STACK LENGTH")
    #     visited = set()
    #     # While there is stuff in the queue/stack
    #     while queue.size() > 0:
    #     #    Pop the first item
    #         path = queue.dequeue()
    #         vertex = path[-1]
    #         # print(vertex, "VERTEX")
    #     #    If not visited
    #         if vertex not in visited:
    #             # print(f"vertex {vertex} not in visted")
    #             if vertex == starting_node:
    #                 # Do the thing!
    #                 # print(path, "PATH")
    #                 return path
    #             # else:
    #             #     return -1
    #             # visited.add(vertex)
    #     # #       For each edge in the item
    #     #         for next_vert in self.get_neighbors(vertex):
    #     #         # Copy path to avoid pass by reference bug
    #     #             new_path = list(path) # Make a copy of path rather than reference
    #     #             new_path.append(next_vert)
    #     #             stack.push(new_path)
    # return -1

    # def earliest_ancestor(ancestors, starting_node):
    #     # Create a queue/stack as appropriate
    # graph = Graph()
    # queue = Queue()
    # # Put the starting point in that
    # # Enstack a list to use as our path
    # for ancestor in ancestors:
    #     # print(ancestor)
    #     queue.enqueue(ancestor)
    #     # Make a set to keep track of where we've been
    #     # for item in stack.stack:
    #     #     print(item, "ITEM IN STACK")
    #     # print(len(stack.stack), "STACK LENGTH")
    #     visited = set()
    #     # While there is stuff in the queue/stack
    #     while queue.size() > 0:
    #     #    Pop the first item
    #         path = queue.dequeue()
    #         vertex = path[-1]
    #         # print(vertex, "VERTEX")
    #     #    If not visited
    #         if vertex not in visited:
    #             # print(f"vertex {vertex} not in visted")
    #             if vertex == starting_node:
    #                 # Do the thing!
    #                 # print(path, "PATH")
    #                 # return path
    #                 visited.add(vertex)
    #         #       For each edge in the item
    #                 for next_vert in get_neighbors(vertex):
    #                 # Copy path to avoid pass by reference bug
    #                     new_path = list(path) # Make a copy of path rather than reference
    #                     new_path.append(next_vert)
    #                     queue.enqueue(new_path)

    #         return path
    # return -1
   

#    def earliest_ancestor(ancestors, starting_node):
    #     # Create a queue/stack as appropriate
    # graph = Graph()
    # queue = Queue()
    # # Put the starting point in that
    # # Enstack a list to use as our path
    # for ancestor in ancestors:
    #     # print(ancestor)
    #     queue.enqueue([ancestor])
    #     # Make a set to keep track of where we've been
    #     # for item in stack.stack:
    #     #     print(item, "ITEM IN STACK")
    #     # print(len(stack.stack), "STACK LENGTH")
    #     visited = set()
    #     # While there is stuff in the queue/stack
    #     while queue.size() > 0:
    #     #    Pop the first item
    #         path = queue.dequeue()
    #         vertex = path[-1]
    #         # print(vertex, "VERTEX")
    #     #    If not visited
    #         if vertex not in visited:
    #             # print(f"vertex {vertex} not in visted")
    #             if vertex == starting_node:
    #                 # Do the thing!
    #                 # print(path, "PATH")
    #                 return path
    #                 visited.add(vertex)
    #         #       For each edge in the item
    #                 # for next_vert in get_neighbors(vertex):
    #                 # # Copy path to avoid pass by reference bug
    #                 #     new_path = list(path) # Make a copy of path rather than reference
    #                 #     new_path.append(next_vert)
    #                 #     queue.enqueue(new_path)

    #         # return path
    # return -1
   