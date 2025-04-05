import pytest

from nebula.data_structures import BinarySearchTree, BinaryTree


# Basic Tree Fixtures
# -----------------
@pytest.fixture
def empty_binary_tree():
    """Empty binary tree for testing initial state and basic operations"""
    return BinaryTree()


@pytest.fixture
def empty_bst():
    return BinarySearchTree()


@pytest.fixture
def sample_tree():
    return BinaryTree.from_iterable([5, 3, 7, 2, 4])


@pytest.fixture
def sample_bst():
    return BinarySearchTree.from_iterable([5, 3, 7, 2, 4])


# Balanced Tree Fixtures
# -------------------
@pytest.fixture
def balanced_bst():
    """
    Creates a perfectly balanced BST with shape:
         4
       /   \
      2     6
     / \   / \
    1   3 5   7
    """
    return BinarySearchTree.from_iterable([4, 2, 6, 1, 3, 5, 7])


# Unbalanced/Special Case Fixtures
# -----------------------------
@pytest.fixture
def unbalanced_bst():
    # Creates an unbalanced BST
    bst = BinarySearchTree()
    for i in range(5):
        bst.insert(i)
    return bst


@pytest.fixture
def skewed_binary_tree():
    """
    Creates a right-skewed tree for testing edge cases:
    1
     \
      2
       \
        3
         \
          4
    """
    tree = BinaryTree()
    for i in range(5):
        tree.insert(i)
    return tree


@pytest.fixture
def convertible_binary_tree():
    return BinaryTree.from_iterable([4, 2, 6, 1, 3, 5, 7])


@pytest.fixture
def complete_binary_tree():
    """Creates a complete binary tree with 7 nodes"""
    tree = BinaryTree()
    for i in range(1, 8):
        tree.insert(i)
    return tree
