'''
There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
Output: 4
Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.

0 - [1,3]
1 - [2,3]

Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
Output: 5
Explanation: There are 5 roads that are connected to cities 1 or 2.

0-(1,3) - 2
1-(0,2,3) - 2 + (3 - 1)
2-(1,3,4)
3-(0,1,2)
4-(2)




Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
Output: 5
Explanation: The network rank of 2 and 5 is 5. Notice that all the cities do not have to be connected.

'''
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        """
        n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
        
        
        |0| -> 1 ,3 
        |1| -> 2 ,3 ,0
        |2| -> 1 
        |3| -> 0 , 1 
        
        Steps
        1. chnage lists to a-list
        
        for every possible combinations of 2 nodes/cities find the total number of cities they are connected to 
        
        key track of the max of those combinations
        
        """
        max1 = float("-inf")
        #chnage to a-list
        graph = {}
        for i in range(n):
            graph[i] = set()
        for city in roads:
            graph[city[0]].add(city[1])
            graph[city[1]].add(city[0])
            
        # find all possible combinations of 2 cities
        for i in range(n): 
            for j in range(n):
                if i == j:
                    continue
                total = 0
                if i in graph[j]: # checks if the noddes are ajacent 
                    total = -1
                city1 = graph[i]
                city2 = graph[j]
                total += len(city1) + len(city2) # calculates the number of outgoing edges between two cities
                max1 = max (total , max1)
        return max1
  
    

