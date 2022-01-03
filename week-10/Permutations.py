"""

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
Accepted
981,784
Submissions
1,399,316


"""


class Solution:
    ans = []
    def permute(self, nums):
        seen = []
        ans = []
        self.originalLenght = len(nums)
        self.permuteHelper(nums , seen, ans)
        return ans
        
        
    def permuteHelper(self , nums , seen, ans):
        self.indent(len(seen))
        print("PermuteHelper(self,", "nums: ",nums ,",", "seen: ", seen,",",  "ans: ",self.ans,")")
        if nums == []:
            ans.append(seen.copy())
        else:
            for i in range(len(nums)):
                chosen = nums[i]
                del nums[i]
                seen.append(chosen)
                self.permuteHelper(nums , seen, ans)
                seen.remove(chosen)
                nums.insert(i,chosen)
    def indent(self,lenght):
        for i in range(lenght):
            print("  ", end="")

    
                
        
        