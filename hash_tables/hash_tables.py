table = [0 for i in range(98)]


def hash_table(key, value):
    hash = key % 97
    table[hash] = value


def read_hash_table(key):
    hash = key % 97
    return table[hash]


def test_storing_value_in_hash_table():
    hash_table(key=1, value='value for one')
    assert read_hash_table(key=1) == 'value for one'


def test_storing_value_that_bigger_than_value_returned_from_hash_func():
    hash_table(key=98, value='bigger')
    assert read_hash_table(key=1) == 'bigger'
