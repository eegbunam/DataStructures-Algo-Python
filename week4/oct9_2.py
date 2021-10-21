"""
Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Return a list of lists of the elements in each vertical level, from left to right and top to bottom in each list.


Input:    1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [[5], [3], [1, 3], [2], [9]]

Input:    3
         / \
        9   20
           /  \  
          15   7

Output: [[9], [3, 15], [20], [7]]

 
Input:    1
        /   \
       2     3
      / \    / \  
     4   5  6   7

Output: [[4],[2],[1,5,6],[3],[7]] or [[4],[2],[1,6,5],[3],[7]]

1 -> (0,0)
2 -> (-1,-1)
4 -> (-2,-2)
5 -> (0,-2)

3 -> (1,-1)
6 -> (0,-2)
7-> (2,-2)
"""
