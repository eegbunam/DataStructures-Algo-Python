'''
BSTs are special in that for each node, all nodes to the left are less than or equal to it, and all nodes to the right are greater than it. Due to this property, lookups in a BST take O(logN) time on average if the tree is well-balanced.

Best cases: Accessing / Searching : O(logN) Inserting: O(logN) Deleting: O(logN)

Worst cases: Accessing / Searching : O(n) Inserting: O(n) Deleting: O(n)

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
# A utility function to insert
# a new node with the given key
 
 
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root
 
# A utility function to do inorder tree traversal
 
 
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
 
 
# Driver program to test the above functions
# Let us create the following BST
#    50
#  /     \
# 30     70
#  / \ / \
# 20 40 60 80
 
r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
 
'''



class BST:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None



  
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


 #recursive printing

def preOrder(root):
  if root is None:
    return
  else:
    print(root.val)
    preOrder(root.left)
    preOrder(root.right)

#preOrder(r)

def inOrder(root):
  if root is None:
    return 
  inOrder(root.left)
  print(root.val)
  inOrder(root.right)
 
#inOrder(r)
  

def itrativePreorder(root):
  stack = []
  stack.append(root)
  while(stack):
    print(stack)
    node = stack.pop()
    print(node.val)
    if node.right:
      stack.append(node.right)
    if node.left:
      stack.append(node.left)
  return



#itrativePreorder(r)

def iterativeInOrder(root):
  stack = []
  current = root

  while (current or stack ):
    while current: #go all the way to the lef
      stack.append(current)
      current = current.left
    # gone all the way to the left end and current is now null
    if stack:
      current = stack[-1] # set current to what it was just before null
      stack.pop() #pop current of the stack because current is set
      print(current.val)
      current = current.right #check the right sub tree
    

  


#iterativeInOrder(r)



def postOrder(root):
  if root is None:
    return
  postOrder(root.left)
  postOrder(root.right)
  print(root.val)

#postOrder(r)


def iterativePostOrder(root):
  """
  still working on this
  
  """
  stack = []
  current = root
  
  while current or stack :

    while current:
      current = current.left
      stack.append(current)
    

    if stack:
      current = stack[-1]
      if current.right:
        current = current.right
      else:
        print(current.val)
        stack.pop()


# Driver program to test the above functions
# Let us create the following BST
#    50
#  /     \
# 30     70
#  / \   / \
# 20 40 60 80
 
#iterativePostOrder(r)
[[50],[30,70], [20,40,60,80]]
def levelOrder(root):
  queue = []
  queue.append(root)
  arr = []
  level = 0

  while(queue):
    size = len(queue)
    #node = queue.pop(0)\
    temp = []
    while size > 0:
      node = queue.pop(0)
      temp.append(node.val)
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
      size-=1
    arr.append(temp)
    level += 1 
  print(arr)
  return arr

levelOrder(r)


# def levelOrder_helper(root):
#     queue = []
#     queue.append(root)
#     arr = []
#     level = 0
#     while(queue):
#         size = len(queue)
#         while size > 0:
#             node = queue.pop(0)
#             if node:
#                 if len(arr) <= level:
#                     arr.insert(level,[node.val])
#                 else:
#                     arr[level].append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             size-=1
#         level += 1 
#     print(arr)
#     return arr


# def levelOrder(root):
#   queue = []
#   queue.append(root)
#   arr = []
#   level  = 0
#   while(queue):
#     node = queue.pop(0)
#     stack = []
#     while(node):
#       if node.left:
#         queue.append(node.left)











  # while(queue):
  #   node = queue.pop(0)
  #   print(node.val)
  #   if node.left:
  #     queue.append(node.left)
  #   if node.right:
  #     queue.append(node.right)
  #   level+= 1
  # #arr.inset(temp,level)
  # print(arr)



    





  
  #iterative printing

  #recursive printing

  #searching

  #building bst 

  #balancing bst

"""
Height of a tree = # of edges in longest path from the node to the leaf node
Height of a tree with one node is 0

"""

def binarySearch(values , key):
  pass



