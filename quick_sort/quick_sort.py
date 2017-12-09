# wycinać array a nie przekazywać normalnie
def quick_sort(array, first_index, last_index):
    import ipdb; ipdb.set_trace()
    partitioned_array, pivot_position = partition(array)
    if len(partitioned_array) > 1:
        quick_sort(partitioned_array[first_index:pivot_position-1], first_index, pivot_position - 1)
        quick_sort(partitioned_array[pivot_position+1:last_index], pivot_position + 1, last_index)
    return partitioned_array


def partition(array):
    pivot = array[len(array) // 2]
    array[len(array) // 2], array[len(array) - 1] = array[len(array) - 1], array[len(array) // 2]
    i = 0
    j = 0
    while i < len(array) - 1:
        if array[i] <= pivot:
            array[i], array[j] = array[j], array[i]
            j += 1
        i += 1
    array[len(array) // 2], array[len(array) - 1] = array[len(array) - 1], array[len(array) // 2]
    return array, j


# def test_partition_complex():
#     assert partition([7, 2, 4, 7, 3, 1, 4, 6, 5, 8, 3, 9, 2, 6, 7, 6, 3]) == \
#         [2, 4, 3, 1, 4, 3, 3, 2, 5, 8, 7, 9, 6, 6, 7, 6, 7]
def test_quick_sort():
    assert quick_sort([3, 4, 1, 2], 0, 3) == [1, 2, 3, 4]
