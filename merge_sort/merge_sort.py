def merge_sort(list_to_sort):
    if len(list_to_sort) <= 1:
        return list_to_sort

    diving_point = len(list_to_sort) // 2
    first_part = merge_sort(list_to_sort[:diving_point])
    second_part = merge_sort(list_to_sort[diving_point:])

    sorted_list = []
    i = 0
    j = 0
    while first_part or second_part:
        if first_part[i] > second_part[j]:
            sorted_list.append(second_part.pop(j))
        else:
            sorted_list.append(first_part.pop(i))

        if not first_part or not second_part:
            sorted_list.extend(first_part or second_part)
            break
    return sorted_list


def test_merge_sort():
    assert merge_sort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]


def test_merge_sort_on_empty_list():
    assert merge_sort([]) == []


def test_merge_sort_on_one_item_list():
    assert merge_sort([1]) == [1]


def test_merge_sort_on_two_item_list():
    assert merge_sort([2, 1]) == [1, 2]


def test_merge_sort_on_random_numbers():
    import random
    list_to_sort = random.sample(range(1, 100), 99)
    assert merge_sort(list_to_sort) == sorted(list_to_sort)
