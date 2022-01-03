"""
Problem #1: Evaluate Division

You are given an array of variable pairs 'equations' and an array of real numbers 'values', where equations[i] = [Ai, Bi] and values[i] represent the equation A_i / B_i = values[i]. Each A_i or B_i is a string that represents a single variable.

You are also given some queries, where queries[j] = [C_j, D_j] represents the jth query where you must find the answer for C_j / D_j = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

EXAMPLES:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Our examples:
["a","b"]
[2.0]
queries = [["a","b"], ["b","a"]]
a ----> b
  <----
a/b = 2, b/a = 1/2

BFS or DFS, graph problem

#create an adjancency list {}

{
  a -> b, c 
  b -> c,
  bc -> cd,
}

node, prev_weight = popleft()
for neighbors in grpah[node]:
  if (node,neighbor) in weights:
    weight = weights[(node,neighbor)]
    q.append(neigbhor , weight*prev_weight)
    
#{a, b : 2.0}
#{b, a : 1/2.0}
#{b, c: 3.0}
#{c, b: 1/3.0}

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]


#loop through all the queries
#start BFS at starting nodes query[0] --> query[1]
#track visited -- set()

#
#base case 1: if start node is not in adjancency list:
#   return -1
#base case 2: we reached our target node "c"
#    return the edge weight
#add start node to visited
#loop through all the neighbors in our adjanceny list:
#    "recursive result" = recursively call on the neighbor node if not visited (update the start, end, visited set)
#   return product of current edge * "recursive result" if not -1
#return -1

"""

from collections import defaultdict
def evaluateDivision(equations:List[List[str]], values: List[int], queries:List[List[str]]) -> int:
  #build adjancency list
  graph, weight = createGraph(equations, values)
  print(graph , weight)
  visited = set()
  res = []
  for query in queries:
    path_length = getBFS(graph, query[0], query[1], visited)
    res.append(path_length)

  return res

def getBFS(graph, start, end, visited) -> int:
  if start not in graph:
    return -1

  if end in graph[start]:
    #return edge value
    return graph[start][end]
  
  visited.add(start)
  for neighbor in 
    


def buildGraph(equations, values):
  graph = {}
  for equation, value in zip(equations, values):
    u, v = equation[0], equation[1]
    if u not in graph: 
      graph[u] = {}
    graph[u][v] = value
    if v not in graph: 
      graph[v] = {}
    graph[v][u] = 1 / value

  return graph



  

# this solution passed leetcode cases
from collections import defaultdict
class Solution:
  #helper function to create graph
    def createGraph(self, edges, values):
        graph = defaultdict(list)
        weights = {}
        for index ,node in enumerate(edges):
            weights[(node[0],node[1])] = values[index]
            weights[(node[1],node[0])] = 1/values[index]
            graph[node[0]].append(node[1])
            graph[node[1]].append(node[0])
        print(graph , weights)
        return (graph, weights)
    
    #helper bfs function 
    def evalDiv(self , start , end, weights, graph):
        visited = set()
        queue = [(start , 1)]
        while(queue):
            node , prev_weight = queue.pop(0)
            visited.add(node)
        
            print(node ,end, prev_weight)
            if node == end:
                return prev_weight
            for neighbor in graph[node]:
                if neighbor not in visited:
                    weight = weights[(node,neighbor)]
                    queue.append((neighbor, weight*prev_weight))
        return -1
                
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        #create graph
        graph, weights = self.createGraph(equations,values)
        known = set()
        # add all possible keys to set
        for key in graph:
            known.add(key)
        
        # loop through queries and 
        result = []
        for querie in queries:
            start = querie[0]
            end = querie[1]
            if start not in known or end not in known:
                result.append(float(-1))
            else: 
                n = self.evalDiv(start, end, weights , graph)
                result.append(n)
        return result
            
        
        
        
        
        
        



