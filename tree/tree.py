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

    def edge(self, start, end):
        if start.left_child == end or start.right_child == end:
            return True
        elif end.children[0] == start or end.children[1] == start:
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
