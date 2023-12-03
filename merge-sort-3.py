from typing import List
from collections import deque
import math

def mergeSort3(numbers: List[int], l: int=0, r:int=None) -> None:
  """
  Sort the given array in place using a modified merge sort that splits the array into thirds 
  instead of halves.

  Runtime: O(nlog_3(n))
  """
  # This function was called with no value for r.
  if r is None:
    # Set r to the length of numbers.
    r = len(numbers)

  # One element in this subarray.
  if r - l <= 1:
    # No need to merge one element.
    return
  
  # Middle-left and middle-right indexes.
  m_l = l + (r - l) // 3
  m_r = l + (r - l) * 2 // 3
  
  # Run recursively on the left, middle, and right subarrays.
  mergeSort3(numbers, l, m_l)
  mergeSort3(numbers, m_l, m_r)
  mergeSort3(numbers, m_r, r)

  # Merge the left, middle, and right subarrays.
  merge(numbers, l, m_l, m_r, r)

def merge(numbers: List[int], l: int, m_l: int, m_r: int, r: int) -> None:
  """
  Merge the sorted subarrays and store the result in the given array.
  """
  # Store the numbers in each subarray as a deque for O(1) pop from front.
  left = deque(numbers[l:m_l])
  middle = deque(numbers[m_l:m_r])
  right = deque(numbers[m_r:r])

  # For every element to be sorted.
  for i in range(r - l):
    # Get the minimum values from the left, middle, and right subarrays.
    # If there are no more elements in a subarray, set the minimum value to infinity so it is never 
    # chosen.
    minimum_left = left[0] if len(left) > 0 else math.inf
    minimum_middle = middle[0] if len(middle) > 0 else math.inf
    minimum_right = right[0] if len(right) > 0 else math.inf
   
    # Get the minimum value across the three subarrays.
    minimum_value = min((minimum_left, minimum_middle, minimum_right))

    # Left subarray has the minimum value.
    if minimum_value == minimum_left:
      # Pop the minimum value from the left subarray and store it in numbers.
      numbers[l + i] = left.popleft()

    # Middle subarray has the minimum value.   
    elif minimum_value == minimum_middle:
      # Pop the minimum value from the middle subarray and store it in numbers.
      numbers[l + i] = middle.popleft()

    # Right subarray has the minimum value.
    elif minimum_value == minimum_right:
      # Pop the minimum value from the right subarray and store it in numbers.
      numbers[l + i] = right.popleft()

# A list with the values [10..1].
ten = list(range(10, 1, -1))

# Print the array before it is sorted.
print(ten)
# >> [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Sort the array in-place.
mergeSort3(ten)

# Print the array after it is sorted.
print(ten)
# >> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
