from heapq import heappop, heappush
from math import inf
from timeit import default_timer as timer

graph = {
        'A': [('B', 10), ('C', 3)],
        'C': [('D', 2), ('B',2)],
        'D': [('E', 10)],
        'E': [('A', 7)],
        'B': [('C', 3), ('D', 2)]
    }


def dijkstras(graph, start):
  distances = {}
  
  for vertex in graph:
    distances[vertex] = inf
    
  distances[start] = 0
  vertices_to_explore = [(0, start)]
  
  while vertices_to_explore:
    current_distance, current_vertex = heappop(vertices_to_explore)
    
    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight
      
      if new_distance < distances[neighbor]:
        distances[neighbor] = new_distance
        heappush(vertices_to_explore, (new_distance, neighbor))
        
  return distances

def dijkstras_without_min_heap(graph, start):
  distances = {}
  
  for vertex in graph:
    distances[vertex] = inf
    
  distances[start] = 0
  vertices_to_explore = [(0, start)]
  
  while vertices_to_explore:
    current_distance, current_vertex = vertices_to_explore.pop(-1) # removing last item from the list
                                                                    # can be also random
    
    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight
      
      if new_distance < distances[neighbor]:
        distances[neighbor] = new_distance
        vertices_to_explore.append((new_distance, neighbor))
        
  return distances
        
start = timer()
distances_from_d = dijkstras(graph, 'A')
print("\n\nShortest Distances: {0}".format(distances_from_d))
end = timer()
print(f'time wth min heap: {end - start}')

start = timer()
distances_from_d = dijkstras_without_min_heap(graph, 'A')
print("\n\nShortest Distances: {0}".format(distances_from_d))
end = timer()
print(f'time without min heap: {end - start}')

# heap = [('B', 10), ('C', 3)]
# heappush(heap, ('B',3))
# print(heap)