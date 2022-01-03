"""
sort nodes in a graoph from least dependent to most dependent
https://iq.opengenus.org/topological-sort-bfs/
"""


#bfs implementation

def topSort(graph):
  """
  Retruns the topological sort of a directed acyclic graph greatly inspired by kahns algo 
  """
  graph_len = len(graph)
  in_degree = [0] * graph_len
  queue = []
  ordering = [0] * graph_len
# populate in_degree array and add leaf nodes to queue
  for node in graph:
    edges = graph[node]
    for edge in edges:
      in_degree[edge] += 1
  for node in graph:
    if in_degree[node] == 0:
      queue.append(node)

  index = 0
  # start a bfs on the queue and basically iteratively get leaf nodes and add to ordering 
  while(len(queue) > 0):
    node = queue.pop(0)
    ordering[index] = node
    index += 1
    # decrement in_degree count for the indexOf(neighbor) in the in_degree arry
    for neighbor in graph[node]:
      in_degree[neighbor] -= 1
      if in_degree[neighbor] == 0:
        queue.append(neighbor)
  
  if index == graph_len:
    print("A topological sort was formed")
    print(ordering)
  else:
    print("A topological sort was notformed")
    print(ordering)

  return ordering











#dfs implementation