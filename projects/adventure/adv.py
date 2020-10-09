from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

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

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

rooms = {}

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


# put first room in the dictionary with the list of exits
rooms[player.current_room] = player.current_room.get_exits()

# while length of visited rooms < total rooms in graph
while len(rooms) < len(room_graph) - 1:
    # if room is not in visited
    if player.current_room.id not in rooms:
        # set the list of exits to the room in visted dict
        rooms[player.current_room.id] = player.current_room.get_exits()
        # mark the room as visited 
        visited_rooms.add(player.current_room)
        # add to the path
        traversal_path.append(player.current_room.id)
        # if the room has no exits
        while len(rooms[player.current_room.id]) < 1:
            # current room = last room from path
            last_room = traversal_path[-1]
            player.travel(last_room)
    else:
        print("This should contain more paths to explor", rooms[player.current_room.id])
            #  
            last_exit = rooms[player.current_room.id].pop()
            traversal_path.append
    # loop through exits of current room 
        # if exit is not in visted
            # add to path
    # else if room has unexplored exits


print(room_graph)

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
