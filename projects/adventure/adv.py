# 1st part build graph - a list with no question marks
# 2nd walk through to visit every room



from room import Room
from player import Player
from world import World
from utils import Queue, Stack

import random
from ast import literal_eval


## most likely don't need to do anything in this file##
# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
# print(player.current_room.id, "ID")
# print(player.current_room.description, "DESCRIPTION")
# print(player.current_room.get_exits(), "EXITS")
# print(player.current_room.n_to, "N to")
# print(player.current_room.s_to, "S to")
# print(player.current_room.w_to, "W to")
# print(player.current_room.e_to, "E to")
# print(player.travel('n'), "PLAYER.TRAVEL")



# Fill this out with directions to walk
# traversal_path = ['n', 'n']

# `player.current_room.id`, `player.current_room.get_exits()` and `player.travel(direction)` useful.

traversal_path = []

# direction = position.get_exits()
# traversal_path.append(direction[-1])

def dft(starting_position):
    """
    Print each vertex in depth-first order
    beginning from starting_vertex.
    """
    # Create a queue/stack as appropriate
    stack = Stack()
    # Put the starting point in that
    stack.push(starting_position.current_room)
    # Make a set to keep track of where we've been
    visited = {}
    
       # While there is stuff in the queue/stack
    while stack.size() > 0:
    #    Pop the first item
        position = stack.pop()
    #    If not visited
        if position.id not in visited:
    #       DO THE THING!
            exits = position.get_exits()
            visited[position.id] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}
            for exit in exits:
                for idx, val in visited[position.id].items():
                    if idx == exit:
                        if idx == 'n':
                            visited[position.id][idx] = position.n_to.id
                        if idx == 's':
                            visited[position.id][idx] = position.s_to.id
                        if idx == 'e':
                            visited[position.id][idx] = position.e_to.id
                        if idx == 'w':
                            visited[position.id][idx] = position.w_to.id
                        

            for next_position in world.rooms:
                stack.push(world.rooms[next_position])
          

                
    return visited


def path(starting_point):
    graph = dft(player)

   
    visited = {} 
    
    if graph:

        s = Stack()
        s.push([starting_point.current_room.id])
        
    
        while s.size() > 0:
            path = s.pop()
            current_room = path[-1]
            count = 0
            random_direction = ''

            if current_room not in visited:
                visited[current_room] = path
                randoms = []
                for idx, val in graph[current_room].items():

                    if val is not '?':
                        randoms.append(idx)
                        random_direction = random.choice(randoms)
                        print(randoms, "RANDOMS LIST")
                    

                if len(random_direction) == 1:
                    if len(traversal_path) == 0:
                        print(random_direction, "line 129")
                        traversal_path.append(random_direction)
                        get_new_room = graph[current_room][random_direction]
                        s.push([get_new_room])
                        random_direction = ''

                    else:
                        traversal_path.append(random_direction)
                        get_new_room = graph[current_room][random_direction]
                        s.push([get_new_room])
                        random_direction = ''


                    # for next_position in graph:

                    #     s.push([next_position])
        
        print(traversal_path, "TRAVERSAL PATH")
        return graph
    


print(path(player))

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")


# def path(starting_point):
#     graph = dft(player)
#     visited = {} 
#     count = 0
#     if graph:

#         queue = Queue()
#         queue.enqueue([starting_point.current_room.id])
    
#         while queue.size() > 0:
#             path = queue.dequeue()
#             current_room = path[-1]

#             if current_room not in visited:
#                 visited[current_room] = path
#                 for paths in graph[current_room]:
#                     if graph[current_room][paths] != '?':
#                         if len(traversal_path) == 0:
#                             traversal_path.append(paths)
#                         elif paths == 'n' and traversal_path[count] == 's' or paths == 's' and traversal_path[count] == 'n':
#                             continue
#                         elif paths == 'w' and traversal_path[count] == "e" or paths == 'e' and traversal_path[count] == "w":
#                             continue
#                         else:
#                             traversal_path.append(paths)
#                             count += 1

#                     for next_position in graph:
#                         # print(next_position, "NEXT POSITION")
#                         queue.enqueue([next_position])
        
#         print(traversal_path, "TRAVERSAL PATH")
#         return graph
    
# def path(starting_point):
#     graph = dft(player)
#     visited = {} 
#     count = 0
#     if graph:

#         s = Stack()
#         s.push([starting_point.current_room.id])
    
#         while s.size() > 0:
#             path = s.pop()
#             current_room = path[-1]

#             if current_room not in visited:
#                 visited[current_room] = path
#                 for paths in graph[current_room]:
#                     if graph[current_room][paths] != '?':
#                         prev_room = current_room - 1
#                         print(f"current_room {current_room}, prev room {prev_room}")
#                         if current_room != current_room - 1:
#                             traversal_path.append(paths)
                            

#                     for next_position in graph:
#                         # print(next_position, "NEXT POSITION")
#                         s.push([next_position])
        
#         print(traversal_path, "TRAVERSAL PATH")
#         return graph