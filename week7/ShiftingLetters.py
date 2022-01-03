"""

You are given a string s of lowercase English letters and an integer array shifts of the same length.

Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

Return the final string after all such shifts to s are applied.

Examples:

Input: s = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: We start with "abc".
After shifting the first 1 letters of s by 3, we have "dbc".
After shifting the first 2 letters of s by 5, we have "igc".
After shifting the first 3 letters of s by 9, we have "rpl", the answer.

Input: s = "aaa", shifts = [1,2,3]
Output: "gfd"

Understand:
Input: s = "aaa", shifts = [1,2,3]
Output: "gfd"

Input: s = "cdfg", shifts = [1,2,3,2] shift[2:]
Output: "shift c 8x, d 7x, f 5x, g 2x"

Match:
Array manipulation problem

Plan:
loop through s and get total number of shifts for each element in s by indexing shifts
update variables appropraitely

lowercase 97 - 122

"zzz" => [2,2,2]

"""
def shiftLetters(s, shifts):
  newStr = ''
  for idx, c in enumerate(s):
    key = sum(shifts[idx:])
    val = ord(c)
    # val = 122
    print(key)
    if val + key > 122: # 125
      key -= (122 - val) # key = 3 -(122-125) => 3 +  3 => 6
      # print(key)
      key = key % 26
      print(key)
      newStr += chr(val + key)
    else:
      newStr += chr(val + key)

  return newStr
  
print(shiftLetters("zzz", [1,1,1]))



def shiftLetter(s, shifts):
  newStr = ''
  for idx, c in enumerate(s):
    key = sum(shifts[idx:])
    val = ord(c) + key 
    if val > 122:
      val = val - 97
      val = val % 26
      val = val + 97
    newStr += chr(val)
  return newStr

print(shiftLetter("zaa", [1,2,3])) 
print(shiftLetter("aaa", [1,2,3]))
print(shiftLetter("cdfg", [1,2,3,2]))

  
