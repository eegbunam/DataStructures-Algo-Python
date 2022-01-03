"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Examples:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Input: s = "catsandog", wordDict = ["cats","dog","sand","and"]
Output: false

Input: s = "leetcode", wordDict = ["leet","code"]

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true

Input: s = "applepenapple", wordDict = ["apple", "lepen"]
Output: False



dp = [False] * (len(s)+1)
wordDict = set(wordDict)
dp[0] = True

loop through s with index i from the start:
    loop through s with  index j
      if s[i:j] in wordDict:
        dp[j] = True
        i = j+1
        j = j+1
return dp[len(s)+1]

"""

#Input: s = "leetcode", wordDict = ["leet","code"]

def lps(s, wordDict):
  wordDict = set(wordDict)
  dp = [False] * (len(s))
  i = 0
  j = 0
  dp[0] = True
  while i < len(s) and  (j < len(s)):
    if j < len(s):
      if (s[i:j+1] not in wordDict):
        j += 1
      else:
        dp[j] = True
        j +=1
        i = j
  return dp[-1]



s = "applepenapple"
wordDict = ["apple", "lepen"]
# Output: False
# wordDict = ["leet","code"]
# s = "leetcode"
print(lps(s , wordDict))


#print(lps("leetcode", ["leet","code"]))







"""
OPT(i) = is there a valid word break j from index 0 to i?

OPT(i) = True if dp[j] = True (0 to j is valid word break) and s[j:i] is in wordDict  
OPT(i) = False otherwise
"""

from typing import List
def wordBreak(s: str, wordDict: List[str]) -> bool:
  word_set = set(wordDict)
  dp = [False] * (len(s) + 1)
  dp[0] = True
  
  for i in range(1, len(s) + 1):
    #if there is a valid word break with string 0...i and s[i:j] in wordDict, then dp[i] = True
    for j in range(i):
      if dp[j] and s[j:i] in word_set:
        dp[i] = True
        break
  return dp[len(s)]

  #O(n^3) / O(n)