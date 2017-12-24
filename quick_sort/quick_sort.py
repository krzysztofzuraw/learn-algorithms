def partition(a):
    q = 0
    j = 0
    r = len(a) - 1
    while j < r:
        if a[j] > a[r]:
            j += 1
        elif a[j] <= a[r]:
            a[j], a[q] = a[q], a[j]
            j += 1
            q += 1
    a[r], a[q] = a[q], a[r]
    return a, q


def quick_sort(a):
    a, q = partition(a)
    return quick_sort(a[0: q])
    return quick_sort(a[q + 1: len(a) - 1])


def test_partition():
    assert partition([12, 7, 14, 9, 10, 11]) == ([7, 9, 10, 11, 14, 12], 3)


def test_partition_more_complex():
    assert partition([9, 7, 5, 11, 12, 2, 14, 3, 10, 6]) == ([5, 2, 3, 6, 12, 7, 14, 9, 10, 11], 3)


def test_quicksort():
    assert quick_sort([12, 7, 14, 9, 10, 11]) == [7, 9, 10, 11, 12, 14]
