Merge sort
==========

This sorting algorithm use divide and conquer technique. It means that first array of items to sort is divided into two pieces, then algorithm
starts to divide pieces until they contain only one piece. Then sorting
step occurs which propagates itself and returned array is sorted.

# Pseudocode

```
merge_sort(array):
    if array.length == 0:
        return array

    first_array = merge_sort(array[0 to array.length / 2])
    second_array = merge_sort(array[array.length /2 to array.length])

    sorted_array = []

    while first_array is not empty and second_array is not empty:
        check every item:
            if item from first_array > item from second_array:
                sorted_array += item from second_array
                remove item from second_array
            else:
                sorted_array += item from first_array
                remove item from first_array
        
        if first_array or second_array is empty:
            sorted_array += first_array or second_array
            exit loop

    return sorted_array
```

# Complexity

As algorithm needs to sort two arrays made from the division. 
One element array can be sorted in fixed time. 
Time for scaling n element array consists of two sums of n/2 arrays + time for sorting half length arrays.

Based on that: worst complexity is O(n log(n)) average: Θ(n log(n)) &
the best: Ω(n log(n))
