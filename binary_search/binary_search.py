def binary_search(array, target):
    low_index = 0
    high_index = len(array) - 1
    while low_index <= high_index:
        mid_index = low_index + (high_index - low_index) // 2
        if array[mid_index] == target:
            return mid_index
        elif array[mid_index] < target:
            low_index = mid_index + 1
        else:
            high_index = mid_index - 1


def test_binary_search():
    assert binary_search([1, 2, 3, 4, 5], 2) == 1


def test_binary_search_non_exisiting_target():
    assert binary_search([3, 4, 5, 6], 7) is None


def test_binary_search_item_at_last_place():
    assert binary_search([1, 2, 3], 3) == 2
