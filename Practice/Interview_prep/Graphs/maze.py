from vertex import Vertex

class Maze:
  def __init__(self):
    self.maze_dict = {}

  def add_vertex(self, node):
    self.maze_dict[node.value] = node

  def add_edge(self, from_node, to_node, weight = 0):
    self.maze_dict[from_node.value].add_edge(to_node.value, weight)
    self.maze_dict[to_node.value].add_edge(from_node.value, weight)

  def explore(self):
    print("Exploring the maze....\n")
    #FILL IN EXPLORE METHOD BELOW
    current_room = 'entrance'
    path_total = 0
    print("\nStarting off at the {0}\n".format(current_room))
    while current_room != 'treasure room':
      node = self.maze_dict[current_room]
      for connected_room, weight in node.edges.items():
        key = connected_room[0]
        print("enter {0} for {1}: {2} cost".format(key,connected_room,weight))
      valid_choices = [key[0] for key in node.edges.keys()]
      print("\nYou have accumulated: {0} cost".format(path_total))
      choice = input("\nWhich room do you move to? ")
      if choice not in valid_choices:
        print("please select from these letters: {0}".format(valid_choices))
      else:
        for room in node.edges.keys():
          if room.startswith( choice):
            current_room = room
            path_total += node.edges[room]
        print("\n*** You have chosen: {0} ***\n".format(current_room))
    print("Made it to the treasure room with {0} cost".format(path_total))

        
  
  def print_map(self):
    print("\nMAZE LAYOUT\n")
    for node_key in self.maze_dict:
      print("{0} connected to...".format(node_key))
      node = self.maze_dict[node_key]
      for adjacent_node, weight in node.edges.items():
        print("=> {0}: cost is {1}".format(adjacent_node, weight))
      print("")
    print("")

def build_graph():
  maze = Maze()
  
  # MAKE ROOMS INTO VERTICES BELOW...
  entrance = Vertex('entrance')
  ante_chamber = Vertex('ante-chamber')
  kings_room = Vertex('king''s room')
  grand_gallery = Vertex('grand gallery')
  treasure_room = Vertex('treasure room')
  # ADD ROOMS TO GRAPH BELOW...
  maze.add_vertex(entrance)
  maze.add_vertex(ante_chamber)
  maze.add_vertex(kings_room)
  maze.add_vertex(grand_gallery)
  maze.add_vertex(treasure_room)

  # ADD EDGES BETWEEN ROOMS BELOW...
  maze.add_edge(entrance,ante_chamber,7)
  maze.add_edge(entrance,kings_room,3)
  maze.add_edge(kings_room,ante_chamber,1)
  maze.add_edge(grand_gallery,ante_chamber,2)
  maze.add_edge(grand_gallery,kings_room,2)
  maze.add_edge(treasure_room,ante_chamber,6)
  maze.add_edge(treasure_room,grand_gallery,4)


  

  # DON'T CHANGE THIS CODE
  maze.print_map()
  return maze
