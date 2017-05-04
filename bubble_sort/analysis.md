Bubble sort
===========

Simple method of comparing two adjacent elements and changing them in place. Sort ends when after next run of algorithm there is no change.

# Pseudocode

```
bubble_sort(array):
  n = array.length
  while n > 1:
    for i in array.length - 1:
      if array[i] > array[i + 1]:
        swap(array[i], array[i+1])
    n = n -1
return array
```

# Complexity

Algorithm starts at the beginning of the array and then compares every 2 items in array. If array is already sorted it still needs to make its run. Based on that the best time complexity is: Ω(n)

The worst time is when array is sorted but in reversed order so algorithm has to check every item: O(n^2)

Based on that complexity of bubble sort is: Θ(n^2)
