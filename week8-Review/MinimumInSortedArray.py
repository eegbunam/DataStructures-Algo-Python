"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.


Undertand:

get the number that would normally be in the first index if the array was not rotated

Intuition/Match:
Use bianry seasrch because we have a series of Trues and Falses (If we compare the each value in the array to the end value) in the array and we need to find the left most False in the array(The first False we find).

Plan:

Bsearch:
  while left < right
    if we see a value greater than end of the array
      move the left = mid+1 
    else:
      move right = mid -1 
eg 
arr =[4,5,6,7,0,1,2] == [TTTTFFF]
T if value > arr[-1]
else False

find first False
"""

def minimumInSortedArray(arr):
  if arr == []: return -1
  left = 0
  right = len(arr) -1

  print("Before While Loop: ",arr[left:right+1])
  
  while left < right:
    print(arr[left:right+1])
    mid = left + (right -left) //2
    if arr[mid] > arr[-1]:
      left = mid + 1
    else:
      right = mid -1
  return arr[left]

arr =[4,5,6,7,0,1,2]
#arr =[1,2,4,5,6,7]
print(minimumInSortedArray(arr))