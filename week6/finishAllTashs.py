"""
There are a total of n tasks you have to pick, labelled from 0 to n-1. Some tasks may have prerequisites, for example to pick task 0 you have to first pick task 1, which is expressed as a pair: [0, 1]

Given the total number of tasks and a list of prerequisite pairs, is it possible for you to finish all tasks?

Input: 2, [[1, 0]] 
Output: true 
Explanation: There are a total of 2 tasks to pick. To pick task 1 you should have finished task 0. So it is possible.

Input: 2, [[1, 0], [0, 1]] 
Output: false 
Explanation: There are a total of 2 tasks to pick. To pick task 1 you should have finished task 0, and to pick task 0 you should also have finished task 1. So it is impossible.

Understand 

To finish all task then a topological ordering should be possible. meaning there is no cycle in the graph

rephrase:
- Find cycle in directed graph


list = Input: 2, [[1, 0], [0, 1]] 

[[nextCourseAfterPrereq , preReq]] 

graph

{
  preReq : [nextCourseAfterPrereq]
}

Match
 graph problem , cycle detection and topological sorting

Implement
  - create a graph -> make an adjacency list
  - use dfs to check for cycle(important)
    - if there is a cycle then we cannot complete the courses listed 
    - else we can complete the courses

    {
      0.      visitingstates == [0,0]
      1

      3 
    }
    pseudocode

      visitingStates [0] * len(graph) 
      visited = 2 
      visiting = 1 
      unvisited = 0

      loop through the graph nodes:
        if visted[node] == univisited:
          start dfs(node visited graph)
      dfs(node visited graph):
        if visitingstates[node] == univisited:
          visitingstates[node] = visiting
          for edge in graph[node]:
            noCyle = dfs(edge , visitedSates , graph)
            visitingStates[edge] = visited
            if noCyle:
              return True
            else:
              return False
        elif visitingstates[node] == visited:
          return True
        elif visitingstates[node] == visiting:
          return False
        return True
        
"""

"""
Implementation
"""

def isCycle(graph):
  pass