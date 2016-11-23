def bubble_sort(array):
    n = len(array)
    while n > 1:
        for i in range(len(array) -1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        n = n - 1
    return array


def test_simple_example():
    assert bubble_sort([4,2,5,1,7]) == [1,2,4,5,7]
