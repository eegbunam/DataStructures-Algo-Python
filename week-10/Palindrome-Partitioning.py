"""

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

Examples:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Input: s = "a"
Output: [["a"]]


loop through the string
  check if current substring is a palindrome
    add to result
    recurse on the next index
dfs(0) 


dfs(index,s, res):

if index >= len(s):
    finalResult.appened(res)
    return

  for charIndex in range(index , len(s));
    if isPalindorome(s[index:charIndex+1])
        res.append(s[index:charIndex+1])
        dfs(charIndex+1)
        res.pop()

dfs(0 , aab ,[]) 
  charIndex = 0
  isPalindrome(s[0:0] = a) => True
  res = [a]
  dfs(1 ,aab , [a,])
    charIndex = 1
    isPalindrome(s[1:1] = a) => True
    dfs(2 , aab , [a,a,])
      charIndex = 2
      isPalidrome(s[2:2] = b) => True
      dfs(3, aab , [a,a,b])
        3 == len(s)
          finalResult.appened([a,a,b])
          go back up
      charIndex = 2
      res.pop() res = [ a ,a]

      nextIteration , charIndex = 3 
      res.pop() [a]
      returns up
    nextInteration, charIndex = 2 index = 1 , res = []
    isPalidrome(s[1:2] = ab) => false
  nextIteration for 0, isPalidrome([s[0:1]] == aa ) True , CharIndex = 1
  res.append ([aa])
  dfs(2 ,aab , res = [aa ,] )
    isPalidrome(s[2:2] = b) => True 
    res.append(b) res = [ aa , b]
    dfs(3)
      finalResult.append(res)
      return back up
    res.pop() removes b 
isPalidrome(s[0:2]) = False ... exit
 
"""


def PalidromePartision(s):

  res = []
  finalResult = []

  def dfs(index , s , res):
    if index >= len(s):
      finalResult.append(res)
      return

    for charIndex in range(index , len(s)):
      if isPalidrome(s[index:charIndex+1]):
        res.append(s[index:charIndex+1 ])
        dfs(charIndex+1 ,s , res)
        res.pop()
      
  dfs(0 ,s,res)
  return finalResult


def isPalidrome(s):
  pass
