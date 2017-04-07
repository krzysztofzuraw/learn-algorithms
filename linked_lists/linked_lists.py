class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return 'Node with {} data'.format(self.data)


class LinkedList(object):
    def __init__(self, head=None):
        self.length = 0
        self.head = head
        self.node_list = []

    def __iter__(self):
        self._add_backward_to_node_list(self.head)
        return self

    def _add_backward_to_node_list(self, first_node):
        if first_node is None:
            return
        head = first_node
        tail = first_node.next_node
        self.node_list.append(head)
        return self.add_backward_to_node_list(tail)

    def __next__(self):
        while self.node_list:
            return self.node_list.pop(0)
        raise StopIteration


def test_node_is_empty():
    node = Node()
    assert node.data is None
    assert node.next_node is None


def test_node_have_data():
    node = Node(data='data')
    assert node.data == 'data'


def test_node_have_reference_to_another_node():
    second_node = Node()
    first_node = Node(next_node=second_node)
    assert first_node.next_node == second_node


def test_linked_list_with_one_node():
    node = Node()
    linked_list = LinkedList(head=node)
    assert [item for item in linked_list] == [node]


def test_linked_list_with_two_nodes():
    first_node = Node(data='first_node')
    second_node = Node(data='second_node')
    first_node.next_node = second_node
    linked_list = LinkedList(head=first_node)
    assert [item for item in linked_list] == [first_node, second_node]
