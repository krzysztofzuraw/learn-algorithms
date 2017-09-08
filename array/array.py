class Array(object):

    def __init__(self, *args):
        self.container = args
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.container[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return item

    def __str__(self):
        container_representation = map(str, self.container)
        return '[{}]'.format(','.join(container_representation))

    def append(self, element):
        self.container = self.container + (element, )


def test_array_representation():
    array_to_represent = Array(1, 2, 3, 4)
    assert str(array_to_represent) == '[1,2,3,4]'

def test_array_can_be_iterable():
    array_to_iter = Array(5, 7, 9)
    results_from_iteration = [item for item in array_to_iter]
    assert results_from_iteration == [5, 7, 9]

def test_array_has_append_method():
    array = Array('string', 1.2)
    array.append(True)
    assert str(array) == '[string,1.2,True]'
