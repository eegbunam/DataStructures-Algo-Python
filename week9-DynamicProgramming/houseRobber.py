"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Examples:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""
#OPT(i) = the maximum amount of money that robber can make from i onwards

#Recurrence:
#Think that you are starting at some house, i. You have two options:
# 1. The robber chooses to rob the current house (gets current money) then can rob from i + 2 onwards 
# 2. the robber chooses to rob the next house (i + 1)
#OPT(i) = max(nums[i] + OPT(i + 1), OPT(i + 1))

#initialization needed:
#Extra cell - 0 (array size n + 1), can't make more money at i + 2
#Last house - nums[n - 1]  (money from last house)
def houseRobber(nums):
  n = len(nums)
  dp = [0] * (n + 1)
  dp[n - 1] = nums[n - 1]
  print(dp)
  for i in range(n - 2, -1, -1):
    dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])

  return dp[0] #max to make from house 1 onwards

print(houseRobber([1,2,3,1]))
