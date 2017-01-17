Bubble sort
===========

Simple method of comparing two adjacent elements and changing them in place. Sort ends when after next run of algoritm there is no change.

# Pseudocode

```
bubble_sort(array):
  n = array.length
  while n > 1:
    for i in array.lenght - 1:
      if array[i] > array[i + 1]:
        swap(array[i], array[i+1])
    n = n -1
return array
```

# Complexity

Algorithm starts at the beginning of the array and then compares every 2 items in array. If array is already sorted it still needs to make its run. Based on that the best time complexity is:

![best_time](http://latex.codecogs.com/gif.latex?%5Cfn_phv%20%5COmega%20%28n%29)

The worst time is when array is sorted but in reversed order so algorithm has to check every item:

![worst_time](http://latex.codecogs.com/gif.latex?%5Cfn_phv%20O%20%28n%29)

Based on that complexity of bubble sort is:

![complexity](http://latex.codecogs.com/gif.latex?%5Cfn_phv%20%5CTheta%20%28n%5E2%29)
