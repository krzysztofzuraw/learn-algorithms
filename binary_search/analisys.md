Binary search
=============

There is an sorted array. The algorithm is looking for the middle value inside. If
the target has the higher value than middle algorithm is looking only for this part of
the array which is higher than the middle element. In case of target being smaller
the algorithm is looking inside the array is taken from the first element till middle one.

This algorithm is using divide and conquer technique.

# Pseudocode

```
def binary_search(array, target):
  low_index = 0, high_index = array.length - 1
  while low_index <= high_index:
    mid_index = low_index + (high_index - low_index) / 2
    if array[mid_index] == target:
      return mid_index
    else if array[mid_index] < target:
      low_index = mid_index + 1
    else:
      high_index = mid_index - 1
```

# Complexity

The best time complexity is when a middle element is the target of the algorithm. In such
case binary search needs to run only once - Ω(1)

As the algorithm is using divide and conquer technique every time is make the wrong
guess the possibilities are cut in half. The algorithm stops after there is
no more array to divide so array length is 1. Binary search also needs to make
first divide so in total n + 1 guesses. In can be written in terms of worst
time complexity - O(log(n))

Based on that complexity of binary search is - Θ(log(n))
