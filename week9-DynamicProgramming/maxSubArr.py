"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Examples:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Input: nums = [1]
Output: 1

Input: nums = [5,4,-1,7,8]
Output: 23


#OPT(i) = the subarray with the largest sum that can be found until i
#At any point i, we can either:
#1. start fresh with the number at index i (new subarray)
#2. add on our number to the existing subarray

Therefore, the reccurence becomes:
OPT(i) = max(nums[i], current_sub + nums[i])

After, we look for the largest value in the array created - this is the max


initialization - the first element of dp can remain the same

Thanks! Just had a dynamic programming exam..

the question I have is how many pointers do we need, i wonder if we can use some pointers to do it 



"""
# nums = [-2,1,-3,4,-1,2,1,-5,4]
#          ^
def subarrayMaximum(nums):
  #initialize the first element? 
  # 
  dp = [0] * (len(nums) + 1)
  dp[0] = nums[0]
  # dp = []
  #maybe:
  for i in range(1, len(nums)):
    dp[i] = max(nums[i], dp[i - 1] + nums[i]) 
  
  #initailize max to lowest possible number than update it in the loop, max subarray could sum to less than 0 
  max_sub = float('-inf') # 
  for j in range(len(dp)):
    max_sub = max(max_sub, dp[j])

  return max_sub


  
print(subarrayMaximum([-2,1,-3,4,-1,2,1,-5,4]))