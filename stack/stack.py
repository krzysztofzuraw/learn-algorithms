import pytest


class Stack(object):
    def __init__(self, maxsize=10):
        self.top = 0
        self.maxsize = maxsize
        self.items = []

    def push(self, item):
        if len(self.items) >= self.maxsize:
            raise StackOverflow
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise StackUnderflow
        item_to_return = self.items[-1]
        self.items.remove(self.items[-1])
        return item_to_return


class StackOverflow(Exception):
    pass


class StackUnderflow(Exception):
    pass


def test_push_stack():
    stack = Stack()
    stack.push(1)
    assert stack.items == [1]


def test_stack_overflow():
    stack = Stack(maxsize=1)
    stack.push(1)
    with pytest.raises(StackOverflow):
        stack.push(2)


def test_pop_stack():
    stack = Stack()
    stack.push(1)
    stack.pop()
    assert stack.items == []


def test_stack_underflow():
    stack = Stack()
    with pytest.raises(StackUnderflow):
        stack.pop()
