def index_equals_value_search(arr):
  """

Given a sorted array arr of distinct integers, write a function indexEqualsValueSearch that returns the lowest index i for which arr[i] == i. Return -1 if there is no such index. Analyze the time and space complexities of your solution and explain its correctness.

Examples:

input: arr = [-8,0,2,5]
output: 2 # since arr[2] == 2

input: arr = [-1,0,3,6]
output: -1 # since no index in arr satisfies arr[i] == i.
Constraints:

[time limit] 5000ms

[input] array.integer arr

1 ≤ arr.length ≤ 100
[output] integer


  [-8,0,2,5]
  
  first iteration
  left = 0
  right = 3
  mid = 1
  arr[mid] = 0 
  
  mid > arr[mid]
    left = mid +1 => 2
  second iteration
  
  left = 2
  right = 3
  
  mid = 2 + (3-2)//2 => 2
  mid == arr[mid] 
    ans = 2
    right = 2
   
 left =2
 right = 2
 false returns
 
  
  
  
  """
  
  if arr == [0]:
    return 0
  left = 0
  right = len(arr) -1
  ans = -1
  while left <= right:
    
    mid  = left + (right - left) //2 
    print("mid:", mid , "arr[mid]" , arr[mid] ,"left ", left , "right ", right)
    if  mid <= arr[mid]:
      if mid == arr[mid]:
        ans = mid
      right = mid-1
      
    else:
      left =  mid +1
  return ans
    
 