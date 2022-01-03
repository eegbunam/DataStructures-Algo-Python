""""

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Examples:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9



"""


# Time O(n) , Space : O(n)
def longestConsecutive(numbers):
  if numbers == []:
    return 0
  seen = set(numbers)
  finalMax = 1
  for index , number in enumerate(numbers):
    curr = number
    currMax = 1
    while curr + 1 in seen:
      currMax+= 1
      curr = curr +1
    finalMax = max(currMax , finalMax)
  return finalMax


print(longestConsecutive([100,4,200,1,3,2]))