"""
Decode Variations
A letter can be encoded to a number in the following way:

'A' -> '1', 'B' -> '2', 'C' -> '3', ..., 'Z' -> '26'
A message is a string of uppercase letters, and it is encoded first using this scheme. For example, 'AZB' -> '1262'

Given a string of digits S from 0-9 representing an encoded message, return the number of ways to decode it.

Examples:

input:  S = '1262'
output: 3
explanation: There are 3 messages that encode to '1262': 'AZB', 'ABFB', and 'LFB'.
Constraints:

[time limit] 5000ms

[input] string S

1 ≤ S.length ≤ 12
[output] integer




"""

#Non optimal backtracking solution. There is a better dynamic programing apporch to this

def decodeVariations(S):
	
  def isDecodable(string):
    if string == "": return False
    alphNumber = int(string)
    return True if (alphNumber >= 1 and alphNumber <= 26) else False

  def decode_helper(index ,string, res):
    if index == len(string):
      res[0] += 1
      return
    else:
      for newIndex in range(index, index+2) :
        currentSpaceString = string[index:newIndex+1]
        if isDecodable(currentSpaceString):
          decode_helper(newIndex+1 , string, res)

  
  
  res = [0]
  decode_helper(0,S,res)
  
  return res[0]

  

    
        
        
        
      
    
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  



