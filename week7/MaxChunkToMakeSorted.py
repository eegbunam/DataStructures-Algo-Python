""""
You are given an integer array arr.

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.

Examples:

[9,7,6,1,4,3]


Input: arr = [5,4,3,2,1]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted. 

U
[5,6,4,3,2,1]
out = 1
[5,6,4]--[3,2,1]
[4,5,6]--[1,2,3]

[4,5,6,1,2,3] X

[1,2,3,4,5]
out = 5
[1],[2],[3],[4],[5]
-->[1,2,3,4,5]
out = 5

[1,2,4,3,6,5]
[1,2]--[4,3]--[6,5]
[1,2]--[3,4]--[5,6]

out = 3

[1,2,3,4,5,6]

HAPPY CASE
Input: [5,4,3,2,1]
Output: 1

HAPPY CASE
Input: [2,1,3,4,4]

Output: 4

EDGE CASE
Input: [1]
Output: 1

Match
Array manipulation, 2-pointers

Plan
set left and right pointers and traverse Array
  count = 0
  max_seen = float("-inf")

  for i in range(len(arr)):
    if arr[i] >= max_seen:
      max_seen = arr[i]
      count += 1
  
  return count



"""


def maxChunkToSort(arr):
  count = 0
  # max_seen = float("-inf")

  for i in range(len(arr)):
    # min([2,0,3], 1) --> min(0,1) = 0
    min_right = min(arr[i:])
    if arr[i] != min_right:
      continue
    # max_seen = arr[i]
    count += 1
  
  return count

arr = [1,2,0,3]
print(arr)