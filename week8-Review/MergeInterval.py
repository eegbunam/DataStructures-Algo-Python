"""

Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Examples:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.



Understand:
-  put intervals in the same timing into one time frame

Match
- regular array problem but sorting will help

Plan
- sort the array based on the starting interval
  if the endVal of current  > start val of the new val
    take the max(endValOfCurent , endValOfNewInterval)

"""

def mergeIntervals(intervals):
  # sort interval by first value in eac interval
  intervals.sort(key = lambda x: x[0])
  merged = [intervals[0]]
  for interval in intervals[1:]:
    #compare lastIntervalEndTime to newIntervalStartTime
    if merged[-1][1] > interval[0]:
      merged[-1][1] = max(merged[-1][1] , interval[1])
    else:
      merged.append(interval)
  return merged

