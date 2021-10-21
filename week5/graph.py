class Graph:
  def __init__(self):
    self.edges = {}

  def add_edge(self, start , end):
    if start not in self.edges:
      self.edges[start] = []
    if end not in self.edges:
      self.edges[end] = []
    self.edges[start].append(end)

  def show(self):
    print(self.edges)

  def changeListTograph(self, lists):
    graph = {}
    for vertex in range(len(lists)):
      graph[vertex] = lists[vertex]
    return graph


  def dfs_print(self,current_vertex):
    # start_vertex = list(self.edges.keys())[0]
    # print(start_vertex)
    visited = [0] * (len(self.edges) + 1)
    visited[current_vertex] = 1
    print(current_vertex)

    for vertex in self.edges:
      self.dfs_print_helper(vertex , visited)

  def dfs_print_helper(self , current_vertex , visted):
    if visted[current_vertex] == 1:
      return
    visted[current_vertex] = 1
    print(current_vertex)
    for edge in self.edges[current_vertex]:
      if visted[edge] == 0:
        self.dfs_print_helper(edge , visted)


    

    
  def bfs_print(self):
    start_vertex = list(self.edges.keys())[0]
    print(start_vertex)
    visited = [0] * (len(self.edges) + 1)
    queue = [start_vertex]
    visited[start_vertex] = 1
    while(queue):
      node = queue.pop(0)
      for edge in self.edges[node]:
        if visited[edge] == 0:
          print(edge)
          visited[edge] = 1
          queue.append(edge)






g = Graph()
g.add_edge(1,2)
g.add_edge(1,4)
g.add_edge(2,1)
g.add_edge(2,3)
g.add_edge(3,2)
g.add_edge(3,4)
g.add_edge(4,1)
g.add_edge(4,3)

#g.show()
#g.dfs_print(list(g.edges.keys())[3])

def changeListTograph(lists):
  graph = {}
  for vertex in range(len(lists)):
    graph[vertex] = lists[vertex]
  return graph

def isBipartite(lists):
  graph = changeListTograph(lists)
  print(graph)
  RED = -1
  BLACK = 1
  colored_vertex = [0] * len(graph) # keep track of the color of vertices
  starting_vertex = list(graph.keys())[0]
  visited = [0] * len(graph) # not visited = 0 and visted = 1
  # visited[starting_vertex] = 1 
  for vertex in graph:
    # for each vertex search the vertex to see if there is a bipartite
    #{0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 3], 3: [0, 2]}
    if visited[vertex] == 0 and isBipartite_helper_dfs(graph,starting_vertex,BLACK,colored_vertex,visited) == False:
      return False
  return True

def isBipartite_helper_dfs(graph , vertex , color , colored_vertex, visited):
 
  if visited[vertex] == 1: # if vertex is visted
    if colored_vertex[vertex] == color: # check to see if vertex has the right color and yes it is so return true
      return True
    else:
      return False # return false if the vertex does not have the correct color
  else:
    visited[vertex] = 1
    colored_vertex[vertex] = color
  for edge in graph[vertex]:
    if isBipartite_helper_dfs(graph,edge,-color,colored_vertex,visited) == False:
      return False
  return True

def isBispartite_helper_bfs():
  pass



graph1 = [[1,2,3],[0,2],[0,1,3],[0,2]]
graph2 = [[1,3],[0,2],[1,3],[0,2]]
print(isBipartite(graph1))
print(isBipartite(graph2))