'''
Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation: 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.

Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.
'''
'''
# Understand
# [[0],[0]] - False
[[2],[1]] - False
[[1,3],[3,0,1],[2],[0]]

visited - [1,0,0,0]
q = []
[0] = visited[0] = 1
0 - 1,3
q = [1,3] - v = [1,0,0,0]
q[3] -      v = [1,1,0,0]
q = []      v = [1,1,0,1]

return False
'''


print("hey")
def keys(rooms):
  n = len(rooms)
  q = []
  visited = [0]* n
  q.append(0)
  visited[0] = 1
  while q:
    i = q.pop()
    if visited[i]!=1:
      visited[i] = 1
    for room in rooms[i]:
      if visited[room]!=1:
        q.append(room)
  if sum(visited)!=n:
    return False
  else:
    return True

print(keys([[1,3],[3,0,1],[2],[0]]))

