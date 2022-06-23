def dfs(graph, current_vertex, target_value, visited=None):
  if visited is None:
    visited = []
	
  visited.append(current_vertex)
  
  if current_vertex == target_value:
    return visited
	
  # Add your recursive case here:
  for neighbor in graph[current_vertex]: 
    if neighbor not in visited:
      path = dfs(graph, neighbor, target_value, visited)
      if path:
        return path

the_most_dangerous_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['lava', 'bees', 'lasers']),
    'piranhas': set(['lava', 'crocodiles']),
    'bees': set(['sharks']),
    'lasers': set(['sharks', 'crocodiles']),
    'crocodiles': set(['piranhas', 'lasers'])
  }

def bfs(graph, start_vertex, target_value):
  path = [start_vertex]
  vertex_and_path = [start_vertex, path]
  bfs_queue = [vertex_and_path]
  visited = set()
  
  while bfs_queue:
    current_vertex, path = bfs_queue.pop(0)
    visited.add(current_vertex)
    
    for neighbor in graph[current_vertex]:
      # Finish the function here:
      if neighbor not in visited:
        if neighbor == target_value:
          return path + [neighbor]
        else:
          bfs_queue.append([neighbor,path+[neighbor] ])

      

# Call bfs() below and print the result:
print(bfs(the_most_dangerous_graph,'crocodiles','bees'))

the_most_dangerous_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['lava', 'bees', 'lasers']),
    'piranhas': set(['lava', 'crocodiles']),
    'bees': set(['sharks']),
    'lasers': set(['sharks', 'crocodiles']),
    'crocodiles': set(['piranhas', 'lasers'])
  }

# print(dfs(the_most_dangerous_graph,'crocodiles','bees'))
print(bfs(the_most_dangerous_graph,'crocodiles','bees'))