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
        full_path = []
        if not start or start == end:
            full_path.append(end)
            return full_path

        full_path.append(start)
        if self.edge(start, start.left_child):
            full_path.extend(self.path(start.left_child, end))
        if self.edge(start, start.right_child):
            full_path.extend(self.path(start.right_child, end))
        return full_path if start and end in full_path else []


@pytest.fixture
def create_tree():
    """
            (2)
           /   \
         (7)   (5)
        /  \     \
      (1)  (6)   (9)
           / \   /
        (5)(11) (4)
    """
    root_node = Node(value=2)
    seventh_node = Node(parent=root_node, value=7)
    fifth_node = Node(parent=root_node, value=5)
    second_node = Node(parent=seventh_node, value=1)
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

    sixth_node.right_child = eleventh_node
    sixth_node.left_child = second_fifth_node

    nineth_node.right_child = fourth_node

    return Tree([
        root_node, seventh_node, fifth_node,
        second_node, sixth_node, nineth_node,
        second_fifth_node, eleventh_node, fourth_node
    ])


def test_root_node(create_tree):
    nodes = create_tree.list_of_nodes
    root_node = nodes.pop(0)
    left_child_node = nodes.pop(0)
    right_child_node = nodes.pop(0)
    assert root_node.left_child == left_child_node
    assert root_node.right_child == right_child_node


def test_children(create_tree):
    nodes = create_tree.list_of_nodes
    root_node = nodes.pop(0)
    left_child_node = nodes.pop(0)
    right_child_node = nodes.pop(0)
    assert root_node.children == (left_child_node, right_child_node)


def test_sibling(create_tree):
    nodes = create_tree.list_of_nodes
    left_child_node = nodes[1]
    right_child_node = nodes[2]
    assert left_child_node.sibling == right_child_node
    assert right_child_node.sibling == left_child_node


def test_leaf(create_tree):
    nodes = create_tree.list_of_nodes
    root_node = nodes[0]
    last_node = nodes[-1]

    assert last_node.is_leaf is True
    assert root_node.is_leaf is False


def test_degree(create_tree):
    nodes = create_tree.list_of_nodes
    root_node = nodes[0]
    nine_node = nodes[-4]
    last_node = nodes[-1]
    assert root_node.degree == 2
    assert last_node.degree == 0
    assert nine_node.degree == 1


def test_edge(create_tree):
    tree = create_tree
    assert tree.edge(tree.list_of_nodes[0], tree.list_of_nodes[1]) is True
    assert tree.edge(tree.list_of_nodes[1], tree.list_of_nodes[0]) is True


def test_edge_more_complex(create_tree):
    tree = create_tree
    assert tree.edge(tree.list_of_nodes[1], tree.list_of_nodes[2]) is False
    assert tree.edge(tree.list_of_nodes[0], tree.list_of_nodes[2]) is True


def test_edge_non_existing(create_tree):
    tree = create_tree
    assert tree.edge(tree.list_of_nodes[1], tree.list_of_nodes[-1]) is False


def test_path_for_left_child(create_tree):
    tree = create_tree
    assert tree.path(tree.list_of_nodes[0], tree.list_of_nodes[3]) == [
        tree.list_of_nodes[0], tree.list_of_nodes[1], tree.list_of_nodes[3]
    ]


def test_path_for_right_child(create_tree):
    tree = create_tree
    assert tree.path(tree.list_of_nodes[0], tree.list_of_nodes[5]) == [
        tree.list_of_nodes[0], tree.list_of_nodes[2], tree.list_of_nodes[5]
    ]


def test_path_for_both_left_and_right(create_tree):
    tree = create_tree
    assert tree.path(tree.list_of_nodes[1], tree.list_of_nodes[6]) == [
        tree.list_of_nodes[1], tree.list_of_nodes[4], tree.list_of_nodes[6]
    ]
