Linear search
=============

Linear search is a method of finding target value in a array. Algorithm checks
every element of array in succession. When value is found algorithm returns
target.

# Pseudocode

```
linear_search(array, target):
  for i = 0 to array.length:
    if array[i] = target:
      return array[i]
```

# Complexity

Algorithm starts from zero element
and then iterates every one until
if found searched item.

In case the searched element is at index zero algorithm terminates
and return index so this is the best time complexity: Ω(1)

The worst time is when searched element is at the end of array. In
such case linear search has to iterate every element in array: O(n)

Based on that complexity of linear search is: Θ(n)
