import random

import pytest

from nebula.data_structures import AbstractTree, BinarySearchTree, BinaryTree

# Core Tree Behavior Tests
# ----------------------
# These tests verify fundamental tree operations
# and invariants that must hold for all tree types


def test_tree_creation():
    """Verify empty tree initialization"""
    tree = BinaryTree()
    assert tree is not None
    assert len(tree) == 0


def test_tree_insert():
    """Verify single node insertion at root"""
    tree = BinaryTree()
    tree.insert(10)
    assert tree.root.value == 10


# Tree Traversal Tests
# ------------------
# Verification of different tree traversal methods
# and their relationships to tree structure


def test_comprehensive_traversals():
    """
    Test all traversal orders for a known balanced tree structure
    Tree shape for reference:
         4
       /   \
      2     6
     / \   / \
    1   3 5   7
    """
    values = [4, 2, 6, 1, 3, 5, 7]
    tree = BinarySearchTree.from_iterable(values)

    # Each traversal has a specific order guarantee
    assert list(tree.preorder()) == [4, 2, 1, 3, 6, 5, 7]  # root-left-right
    assert list(tree.inorder()) == [1, 2, 3, 4, 5, 6, 7]  # left-root-right
    assert list(tree.postorder()) == [1, 3, 2, 5, 7, 6, 4]  # left-right-root

    # Structure preservation after conversion
    btree = tree.to_binary_tree()
    assert list(btree.preorder()) == [4, 2, 1, 3, 6, 5, 7]  # same structure


# Tree Balance and Structure Tests
# -----------------------------
# Tests focusing on tree shape, balance, and structural properties


def test_binary_tree_default_insert_behavior():
    """
    Verify level-order insertion creates a complete binary tree
    Expected shape for values 1-7:
         1
       /   \
      2     3
     / \   / \
    4   5 6   7
    """
    tree = BinaryTree()
    # Insert values 1 through 7
    for i in range(1, 8):
        tree.insert(i)

    # Verify level-order filling
    assert tree.root.value == 1  # Level 1
    assert tree.root.left.value == 2  # Level 2
    assert tree.root.right.value == 3  # Level 2
    assert tree.root.left.left.value == 4  # Level 3
    assert tree.root.left.right.value == 5  # Level 3
    assert tree.root.right.left.value == 6  # Level 3
    assert tree.root.right.right.value == 7  # Level 3

    # Test that the tree is balanced
    assert tree.height() == 3
    assert BinarySearchTree.is_balanced(tree)


# BST-Specific Tests
# ----------------
# Tests that verify Binary Search Tree properties and operations


def test_bst_auto_balance_parameter():
    """
    Test BST balance behavior with different auto-balance settings
    Note: auto_balance=True should maintain AVL properties
    """
    # With auto_balance=True (default)
    balanced_bst = BinarySearchTree()
    for i in range(5):
        balanced_bst.insert(i)
    assert BinarySearchTree.is_balanced(balanced_bst)

    # With auto_balance=False
    unbalanced_bst = BinarySearchTree(auto_balance=False)
    for i in range(5):
        unbalanced_bst.insert(i)
    assert not BinarySearchTree.is_balanced(unbalanced_bst)

    # Test changing auto_balance after creation
    initially_unbalanced = BinarySearchTree(auto_balance=False)
    for i in range(5):
        initially_unbalanced.insert(i)
    assert not BinarySearchTree.is_balanced(initially_unbalanced)

    # Enable auto-balancing and insert one more element
    initially_unbalanced.auto_balance = True
    initially_unbalanced.insert(5)
    assert BinarySearchTree.is_balanced(initially_unbalanced)


def test_bst_add_operator():
    """
    Test the __add__ operator for merging two BSTs.
    - Ensure the resulting BST contains all unique elements from both trees.
    - Verify that the resulting tree maintains BST properties.
    """
    bst1 = BinarySearchTree.from_iterable([5, 3, 7])
    bst2 = BinarySearchTree.from_iterable([4, 6, 8])

    # Merge the two BSTs
    merged_bst = bst1 + bst2

    # Verify the merged BST contains all unique elements
    expected_values = [3, 4, 5, 6, 7, 8]
    assert list(merged_bst.inorder()) == expected_values

    # Verify the merged BST maintains BST properties
    assert (
        merged_bst.root.value == 5
    )  # Root should be the first inserted value from bst1
    assert merged_bst.root.left.value == 4
    assert merged_bst.root.right.value == 7

    # Verify that the original BSTs remain unchanged
    assert list(bst1.inorder()) == [3, 5, 7]
    assert list(bst2.inorder()) == [4, 6, 8]


# Tree Conversion Tests
# ------------------
# Tests for converting between different tree types while
# preserving various properties


def test_binary_tree_to_bst():
    """
    Test conversion from BinaryTree to BST
    - Should preserve values
    - Should establish BST ordering
    - Can optionally maintain balance
    """
    # Create an unbalanced binary tree
    btree = BinaryTree()
    for i in range(5):  # This creates a right-skewed tree
        btree.insert(i)

    # Convert to BST with auto-balancing
    bst = BinarySearchTree.from_binary_tree(btree)

    # Check if balanced and maintains BST properties
    assert BinarySearchTree.is_balanced(bst)
    assert list(bst.inorder()) == sorted(range(5))

    # Convert to BST without auto-balancing
    unbalanced_bst = BinarySearchTree.from_binary_tree(btree, auto_balance=False)

    # Check if maintains BST properties but remains unbalanced
    assert not BinarySearchTree.is_balanced(unbalanced_bst)
    assert list(unbalanced_bst.inorder()) == sorted(range(5))


# Performance Tests
# --------------
# Tests focusing on performance characteristics and scalability


@pytest.mark.benchmark
def test_tree_large_scale(benchmark):
    """Benchmark tree creation and verify properties at scale"""

    def build_large_tree():
        values = random.sample(range(2000), 1000)  # Random unique values
        return BinarySearchTree.from_iterable(values)

    tree = benchmark(build_large_tree)
    # Verify tree properties after benchmark
    assert len(tree) == 1000
    assert len(list(tree.inorder())) == 1000


# Intermediate Tests
def test_tree_iterable():
    tree = BinaryTree.from_iterable([5, 3, 7, 2, 4])
    assert list(tree) == [2, 3, 4, 5, 7]  # tests __iter__
    assert len(tree) == 5  # tests __len__
    assert 3 in tree  # tests __contains__


def test_tree_traversals():
    tree = BinaryTree.from_iterable([5, 3, 7])
    assert list(tree.inorder()) == [3, 5, 7]
    assert list(tree.preorder()) == [5, 3, 7]
    assert list(tree.postorder()) == [3, 7, 5]


# Advanced Features Tests
def test_tree_operations():
    t1 = BinaryTree.from_iterable([1, 2, 3])
    t2 = BinaryTree.from_iterable([4, 5, 6])
    t3 = t1 + t2  # tests __add__
    assert list(t3) == [1, 2, 3, 4, 5, 6]


def test_tree_slicing():
    tree = BinaryTree.from_iterable(range(10))
    assert list(tree[2:5]) == [2, 3, 4]  # tests __getitem__


# Abstract Tree Tests
def test_abstract_tree_properties():
    tree = BinaryTree()
    assert isinstance(tree, AbstractTree)
    assert hasattr(tree, "children")
    assert len(tree.children) <= 2  # Binary tree specific


def test_binary_tree_properties():
    tree = BinaryTree()
    tree.insert(5)
    assert hasattr(tree.root, "left")
    assert hasattr(tree.root, "right")


# Binary Search Tree Tests
def test_bst_ordering():
    bst = BinarySearchTree()
    values = [5, 3, 7, 2, 4, 6, 8]
    for val in values:
        bst.insert(val)
    assert list(bst.inorder()) == sorted(values)
    assert bst.root.left.value < bst.root.value
    assert bst.root.right.value > bst.root.value


def test_bst_search():
    bst = BinarySearchTree.from_iterable([5, 3, 7, 2, 4])
    assert bst.search(3) is not None
    assert bst.search(6) is None


# Tree Balance Tests
def test_tree_height():
    tree = BinaryTree.from_iterable([5, 3, 7, 2, 4, 6, 8])
    assert tree.height() == 3  # Root level = 1


def test_tree_balance_factor():
    bst = BinarySearchTree()
    values = [5, 3, 7, 2, 4, 6, 8]
    for val in values:
        bst.insert(val)
        # Balance factor should be between -1 and 1 for each node
        assert -1 <= bst.balance_factor() <= 1


def test_unbalanced_tree():
    tree = BinaryTree()
    # Creating deliberately unbalanced tree
    for i in range(5):
        tree.insert(i)  # Insert in order will create right-heavy tree
    assert tree.height() > 3  # Unbalanced tree will be taller
    assert abs(tree.balance_factor()) > 1


@pytest.mark.benchmark
def test_balance_performance(benchmark):
    def build_and_check_balance():
        values = random.sample(range(100), 50)
        tree = BinarySearchTree.from_iterable(values)
        return all(
            -1 <= node.balance_factor() <= 1 for node in tree.nodes()
        )  # Check all nodes are balanced

    assert benchmark(build_and_check_balance)


def test_bst_to_binary_tree():
    bst = BinarySearchTree.from_iterable([4, 2, 6, 1, 3, 5, 7])
    btree = bst.to_binary_tree()

    # Should maintain structure but lose BST properties
    assert isinstance(btree, BinaryTree)
    assert not isinstance(btree, BinarySearchTree)
    assert len(btree) == len(bst)


def test_balance_validation():
    # Test static balance checker
    balanced_tree = BinaryTree.from_iterable([4, 2, 6, 1, 3, 5, 7])
    unbalanced_tree = BinaryTree()
    for i in range(5):
        unbalanced_tree.insert(i)

    assert BinarySearchTree.is_balanced(balanced_tree)
    assert not BinarySearchTree.is_balanced(unbalanced_tree)


def test_bst_maintains_balance():
    bst = BinarySearchTree()
    # Insert in a way that would create an unbalanced tree if not auto-balanced
    values = list(range(10))
    for val in values:
        bst.insert(val)
        assert BinarySearchTree.is_balanced(bst)


def test_bst_conversion_preserves_values():
    values = [5, 3, 7, 2, 4, 6, 8]
    btree = BinaryTree.from_iterable(values)
    bst = BinarySearchTree.from_binary_tree(btree)
    back_to_btree = bst.to_binary_tree()

    # All three should contain the same values
    assert sorted(list(btree)) == sorted(values)
    assert list(bst.inorder()) == sorted(values)
    assert sorted(list(back_to_btree)) == sorted(values)


def test_from_iterable_preserves_preorder():
    # Test for BinaryTree
    input_values = [10, 5, 3, 7, 15, 12, 20]
    tree = BinaryTree.from_iterable(input_values)
    assert list(tree.preorder()) == input_values

    # Test for BinarySearchTree
    bst_values = [8, 4, 2, 6, 12, 10, 14]
    bst = BinarySearchTree.from_iterable(bst_values)
    assert list(bst.preorder()) == bst_values


def test_binary_tree_insert_maintains_complete_property():
    tree = BinaryTree()
    # Insert 1-5 nodes
    for i in range(1, 6):
        tree.insert(i)

    # For 5 nodes, should form a complete binary tree:
    #     1
    #   2   3
    # 4  5
    assert tree.root.value == 1
    assert tree.root.left.value == 2
    assert tree.root.right.value == 3
    assert tree.root.left.left.value == 4
    assert tree.root.left.right.value == 5

    # Verify it's filling left-to-right at each level
    last_level_nodes = list(tree.level_order())[-2:]  # Last two nodes
    assert last_level_nodes == [4, 5]
