
"""
Given a string s, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.

 

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]
Example 3:

Input: s = "12345"
Output: ["12345"]
Example 4:

Input: s = "0"
Output: ["0"]




"""



class Solution:
    ans = []
    def letterCasePermutation(self, s: str):
        self.permute(0,"",s)
        return (self.ans) if s else []
        
    def permute(self,start, curr , s):
        
        for index in range(start , len(s)): 
           
            character = s[index]
            if character.isnumeric():
                curr += character
                continue
            
            lowerCharacter = character.lower()
            print( "In for loop, curr => " ,curr + lowerCharacter, " Going to add this letter next =>" , character,"index =>" , index)
            self.permute(index+1 , curr+lowerCharacter,s)
            
            upperCharacter = character.upper()
            print( "In for loop, curr => " ,curr+upperCharacter, " Going to add this letter next =>" , character, "index =>" , index)
            self.permute(index+1 , curr+upperCharacter,s)
        #print(curr , "out of forr loop")
        if len(curr) == len(s):
            
            self.ans.append(curr)
            return

print(Solution().letterCasePermutation(s="abc"))
# investigate the print statemnts for "a1b2c"

"""

ab out of forr loop
aB out of forr loop
a out of forr loop
Ab out of forr loop
AB out of forr loop
A out of forr loop
b out of forr loop
B out of forr loop
 out of forr loop

In for loop, curr =>  a  Going to add this letter next => a
In for loop, curr =>  ab  Going to add this letter next => b
In for loop, curr =>  aB  Going to add this letter next => b
In for loop, curr =>  A  Going to add this letter next => a
In for loop, curr =>  Ab  Going to add this letter next => b
In for loop, curr =>  AB  Going to add this letter next => b
In for loop, curr =>  b  Going to add this letter next => b
In for loop, curr =>  B  Going to add this letter next => b

"""