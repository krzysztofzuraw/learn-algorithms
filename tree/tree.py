class Node:
    def __init__(self, parent=None, left_child=None, right_child=None, value=None):
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child
        self.value = value

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
        return self.left_child + self.right_child


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
