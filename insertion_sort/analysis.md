Insertion sort
==============

Algorithm that starts from second place in array. Then it looks to first one and
compare it. Thanks to that we are creating sorted list. Then algorithm continues
with other elements. This algorithm is very similar to how people sort cards in
decks.

# Pseudocode

```
insertion_sort(array):
  for i = 1 to array.length:
    key = array[i]
    j = i - 1
    while j >= 0 and array[i] > array[j]:
      swap(array[i], array[j])
      j = j - 1
      i = i - 1
  return array
```

# Complexity

Algorithm starts at the second place of the array
and then compare item that is on
the first place. After this two elements
array is sorted and algorithm
goes into next item and compare it
with already sorted ones. Based
on that the best time complexity
is: Ω(n)

The worst time is when array is sorted but in reversed order so algorithm has to
check every item: O(n^2)

Based on that complexity of insertion sort is: Θ(n^2)
