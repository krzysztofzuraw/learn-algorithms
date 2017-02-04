def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i


def test_linear_search():
    assert linear_search([4, 2, 5, 1, 7], 1) == 3


def test_linear_search_non_existing():
    assert linear_search([2, 1], 4) is None


def test_linear_search_strings():
    assert linear_search(['test_string', 'abc', 'def'], 'def') == 2


def test_linear_search_empty():
    assert linear_search([], 'searchable') is None
