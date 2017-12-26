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
    if len(a) <= 1:
        return a
    a, q = partition(a)
    first_part = quick_sort(a[0: q])
    second_part = quick_sort(a[q: len(a)])
    return first_part + second_part


def test_partition():
    assert partition([12, 7, 14, 9, 10, 11]) == ([7, 9, 10, 11, 14, 12], 3)


def test_partition_more_complex():
    assert partition([9, 7, 5, 11, 12, 2, 14, 3, 10, 6]) == ([5, 2, 3, 6, 12, 7, 14, 9, 10, 11], 3)


def test_quicksort():
    assert quick_sort([12, 7, 14, 9, 10, 11]) == [7, 9, 10, 11, 12, 14]


def test_quicksort_one_element():
    assert quick_sort([1]) == [1]


def test_quicksort_more_complex():
    assert quick_sort([9, 7, 5, 11, 12, 2, 14, 3, 10, 6]) == [2, 3, 5, 6, 7, 9, 10, 11, 12, 14]
