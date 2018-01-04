import pytest


class Node:
    def __init__(self, parent=None, left_child=None, right_child=None, value=None):
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child
        self.value = value

    def __repr__(self):
        return f'Node with value: {self.value}'

    @property
    def children(self):
        return self.left_child, self.right_child

    @property
    def sibling(self):
        if self.parent:
            if self.parent.left_child == self:
                return self.parent.right_child
            else:
                return self.parent.left_child

        return "No parent node"

    @property
    def is_leaf(self):
        return False if self.left_child or self.right_child else True

    @property
    def degree(self):
        if self.left_child and self.right_child:
            return 2
        elif self.left_child or self.right_child:
            return 1
        return 0


class Tree:
    def __init__(self, list_of_nodes=None):
        self.list_of_nodes = list_of_nodes

    @staticmethod
    def edge(start, end):
        if not start or not end:
            return False
        if start.left_child == end or start.right_child == end:
            return True
        elif end.left_child == start or end.right_child == start:
            return True
        return False

    def path(self, start, end):
        if not start or start == end:
            yield end
            raise StopIteration

        yield start
        if self.edge(start, start.left_child):
            yield from self.path(start.left_child, end)
        elif self.edge(start, start.right_child):
            yield from self.path(start.right_child, end)


@pytest.fixture
def create_tree():
    """
            (2)
           /   \
         (7)   (5)
        /  \     \
      (2)  (6)   (9)
           / \   /
        (5)(11) (4)
    """
    root_node = Node(value=2)
    seventh_node = Node(parent=root_node, value=7)
    fifth_node = Node(parent=root_node, value=5)
    second_node = Node(parent=seventh_node, value=2)
    sixth_node = Node(parent=seventh_node, value=6)
    nineth_node = Node(parent=fifth_node, value=9)
    second_fifth_node = Node(parent=sixth_node, value=5)
    eleventh_node = Node(parent=sixth_node, value=11)
    fourth_node = Node(parent=nineth_node, value=4)

    root_node.left_child = seventh_node
    root_node.right_child = fifth_node

    seventh_node.left_child = second_node
    seventh_node.right_child = sixth_node

    fifth_node.right_child = nineth_node

    sixth_node.right_child = second_fifth_node
    sixth_node.left_child = eleventh_node

    nineth_node.right_child = fourth_node

    return Tree([
        root_node, seventh_node, fifth_node,
        second_node, sixth_node, nineth_node,
        second_fifth_node, eleventh_node, fourth_node
    ])


def test_root_node():
    """
            (1)
            /  \
          (3)  (2)
    """
    root_node = Node(value=1)
    left_child_node = Node(parent=root_node, value=2)
    right_child_node = Node(parent=root_node, value=3)
    root_node.left_child = left_child_node
    root_node.right_child = right_child_node
    assert root_node.left_child == left_child_node
    assert root_node.right_child == right_child_node


def test_children():
    """
            (2)
             |
            (5)
    """
    root_node = Node(value=2)
    left_child_node = Node(parent=root_node, value=5)
    root_node.left_child = left_child_node
    assert root_node.children == (left_child_node, None)


def test_sibling():
    """
            (2)
           /  \
         (5)  (7)
    """
    root_node = Node(value=2)
    left_child_node = Node(parent=root_node, value=5)
    right_child_node = Node(parent=root_node, value=7)
    root_node.left_child = left_child_node
    root_node.right_child = right_child_node
    assert left_child_node.sibling == right_child_node
    assert right_child_node.sibling == left_child_node


def test_leaf():
    """
        (1)
         |
        (2)
    """
    root_node = Node(value=1)
    left_child_node = Node(parent=root_node, value=2)
    root_node.left_child = left_child_node
    assert left_child_node.is_leaf is True
    assert root_node.is_leaf is False


def test_degree():
    """
        (1)
       /   \
     (2)   (3)
    """
    root_node = Node(value=1)
    left_child_node = Node(parent=root_node, value=2)
    right_child_node = Node(parent=root_node, value=3)
    root_node.left_child = left_child_node
    root_node.right_child = right_child_node
    assert root_node.degree == 2
    assert left_child_node.degree == 0


def test_degree_more_complex():
    """
        (1)
         |
        (2)
    """
    root_node = Node(value=1)
    child_node = Node(parent=root_node, value=2)
    root_node.left_child = child_node
    assert root_node.degree == 1


def test_edge():
    """
        (1)
         |
        (2)
    """
    root_node = Node(value=1)
    child_node = Node(parent=root_node, value=2)
    root_node.left_child = child_node
    tree = Tree([root_node, child_node])
    assert tree.edge(root_node, child_node) is True
    assert tree.edge(child_node, root_node) is True


def test_edge_more_complex():
    """
        (1)
       /   \
     (2)   (3)
    """
    root_node = Node(value=1)
    left_child_node = Node(parent=root_node, value=2)
    right_child_node = Node(parent=root_node, value=3)
    root_node.left_child = left_child_node
    root_node.right_child = right_child_node
    tree = Tree([root_node, left_child_node, right_child_node])
    assert tree.edge(left_child_node, right_child_node) is False
    assert tree.edge(root_node, right_child_node) is True


def test_edge_non_existing():
    """
        (1)
    """
    root_node = Node(value=1)
    tree = Tree([root_node])
    assert tree.edge(root_node, None) is False


def test_path_for_left_child():
    """
        (1)
         |
        (2)
         |
        (3)
         |
        (4)
    """
    root_node = Node(value=1)
    child_node = Node(parent=root_node, value=2)
    last_node = Node(parent=child_node, value=3)
    four_node = Node(parent=last_node, value=4)
    root_node.left_child = child_node
    child_node.left_child = last_node
    last_node.left_child = four_node
    tree = Tree([root_node, child_node, last_node, four_node])
    assert [i for i in tree.path(root_node, last_node)] == [root_node, child_node, last_node]
    assert [i for i in tree.path(root_node, four_node)] == [root_node, child_node, last_node, four_node]


def test_path_for_right_child():
    """
        (1)
         |
        (2)
         |
        (3)
         |
        (4)
    """
    root_node = Node(value=1)
    child_node = Node(parent=root_node, value=2)
    last_node = Node(parent=child_node, value=3)
    four_node = Node(parent=last_node, value=4)
    root_node.right_child = child_node
    child_node.right_child = last_node
    last_node.right_child = four_node
    tree = Tree([root_node, child_node, last_node, four_node])
    assert [i for i in tree.path(root_node, last_node)] == [root_node, child_node, last_node]
    assert [i for i in tree.path(root_node, four_node)] == [root_node, child_node, last_node, four_node]


def test_path_for_both_left_and_right():
    """
        (1)
        /
       (2)
         \
         (3)
    """
    root_node = Node(value=1)
    second_node = Node(parent=root_node, value=2)
    third_node = Node(parent=second_node, value=3)
    root_node.left_child = second_node
    second_node.right_child = third_node
    tree = Tree([root_node, second_node, third_node])
    assert [i for i in tree.path(root_node, third_node)] == [root_node, second_node, third_node]
