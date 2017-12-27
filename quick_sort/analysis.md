# Quick Sort

In this algorithm divide and conquer technique is used. First we choose pivot
(in this implementation the last element in the array) then we partition array into two subarrays:
one having only items that are less than pivot and the second one with elements above pivot. Then
we recursively call quicksort on both of subarrays.

## Pseudocode

```
def quicksort(a):
    if len(a) <= 1:
        return a
    a,q = partition(a)
    first_part = quick_sort(a[0...q])
    second_part = quick_sort(a[q...len(a)])
    return first_part + second_part

def partition(a):
    p,q,j = 0
    r = len(a) - 1
    while j < r:
        if a[j] > a[r]:
            j++
        elif a[j] =< a[r]:
            swap a[j] and a[r]
            j++
            q++
    swap a[r] and a[q]
    return a,q
```

## Complexity

Worst case: when the pivot is the largest or the smallest element in the array we have to make n - 1
nested calls before reaching 1. It means that the worst case time complexity is O(n^2)

Best case: when we divide list into two equals pieces. To sort we have to make log2(n) nested calls
before reaching 1. It means that the best case time complexity is Ω(n log(n)).

Average case: Based on the best & the worst: Θ(n log(n))

Space complexity: worst - O(log(n))

### References

* [Big O Cheatsheet](http://bigocheatsheet.com/)
* [Wikipedia](https://en.wikipedia.org/wiki/Quicksort)
* [Khanacademy](https://www.khanacademy.org/computing/computer-science/algorithms/quick-sort/a/overview-of-quicksort)
