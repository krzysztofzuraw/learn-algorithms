# Quick Sort


```
def partition(a):
    p,q,j = 0
    r = len(a) - 1
    while j != r:
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

### References
