'''
There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.

Undertand
example: 
input [[2,3,1], 
      [3,3], 
      [1,1,1,1,1,1],
      [5,1]]
output --> [1]

edge case
input [[1,1,1,1,1,1], 
      [1,1,1,1,1,1], 
      [1,1,1,1,1,1],
      [1,1,1,1,1,1]]
output --> [0]

width of wall always == (fixed value)

Match
Hash map
match_variable
Plan  
for each value in array
  forloop to loop through the col to match
    the value
    if gap has been seen:
      increment value
    else:
      add gap with frequency val 1
set match_variable to new gap number if its bigger
find most frequent gap_pos
get height of wall
ans = height of wall - freq

Time_complexity = O(n^2)
Space = O(n)

Implement

Review
'''

def find_gap(wall):
  hash_map = {}
  max_freq = 0
  if len(wall) < 1: ##edge case
      return len(wall)
  for row in wall:
    gap = 0
    for brick in row[:-1]:
      gap += brick
      if gap in hash_map:
        hash_map[gap] += 1
      else:
        hash_map[gap] = 1
      if hash_map[gap] > max_freq:
        max_freq = hash_map[gap]
  return len(wall) - max_freq
    

print(find_gap([[1,1,1,1,1,1], 
      [1,1,1,1,1,1], 
      [1,1,1,1,1,1],
      [1,1,1,1,1,1]]))
    

print(find_gap([[2,3,1], 
      [3,3], 
      [1,1,1,1,1,1],
      [5,1]]))

print(find_gap([[1,2,2,1],
                [3,1,2],
                [1,3,2],
                [2,4],
                [3,1,2],
                [1,3,1,1]]))