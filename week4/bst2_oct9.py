"""


Problem #1: Create balanced BST
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Examples:

Image of balanced bst exampleSource: LeetCode
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:


Input: nums = [-10,-3,0,5,9]

first call
root = 0
left = [-10,-3]
right =  [5,9]


second call on left

root = -3 ( index(-10) + index (-3) / 2 )
left = [-10]
right = []

thrid call on the left

root = -10
left = index(-10) + index(-10) / 2 = []
right = []

root = null 
left = impossible
right = impossible

if left > right:
  return None
get the mid element and make the root
- assign the left elemets from the mid to root.left
- assign the right elements from the mid to root.right
return root

"""


class BST:
  def __init__(self, val):
    self.val = val
    self.left = self.right = None 


"""

nums = [-10,-3,0,5,9]

left = 0
right = 4
mid = 2 , root = 0

recurse on left [-10 , -3]

recurse on right [5,9]

"""
def createBalancedBst(values):
  left , right = 0 , len(values)-1
  root = helper(values, left , right)
  helperPrint(root)
  return root 

def helper(values , left , right):
  if left > right:
    return None
  mid = (left + right) // 2
  val = values[mid]
  root = BST(val)
  root.left = helper(values , left , mid-1)
  root.right = helper(values , mid+1  , right)
  return root 

def helperPrint(root):
  if root is None:
    return 
  print(root.val)
  helperPrint(root.left)
  helperPrint(root.right)
  


def insert(root : BST, val : int) -> BST:
  if root is None:
    return BST(val)
  else:
    if root.val == val:
      return root
    elif val > root.val:
      root.right = insert(root.right,val)
    elif val <  root.val:
      root.left = insert(root.left , val)
  return root


r = BST(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)


def helperLevelOrder(root):

  queue = []
  queue.append(root)
  arr = []
  
  while queue:
    size = len(queue)
    temp = []
    while size > 0:
      node = queue.pop(0)
      if node:
        temp.append(node.val)
        if node.left:
          queue.append(node.left)
        if node.right:
          queue.append(node.right)
      size -= 1  

    arr.append(temp)
  return arr


nums = [-10,-3,0,5,9]
root = createBalancedBst(nums)
print(helperLevelOrder(root))
      

  



