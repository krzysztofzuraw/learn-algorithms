def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[i] < array[j]:
            array[i], array[j] = array[j], array[i]
            j -= 1
            i -= 1
    return array


def test_insertion_sort_simple():
    assert insertion_sort([4, 2, 5, 1, 7]) == [1, 2, 4, 5, 7]


def test_insertion_sort_one_number():
    assert insertion_sort([1]) == [1]


def test_insertion_sort_already_sorted():
    assert insertion_sort([1, 2]) == [1, 2]
