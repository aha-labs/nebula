from nebula.data_structures import BinaryTree
import random


# Basic Tests
def test_tree_creation():
    tree = BinaryTree()
    assert tree is not None
    assert len(tree) == 0


def test_tree_insert():
    tree = BinaryTree()
    tree.insert(10)
    assert tree.root.value == 10
    tree.insert(5)
    assert tree.root.left.value == 5
    tree.insert(15)
    assert tree.root.right.value == 15


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


# Performance Tests
def test_tree_large_scale(benchmark):
    def build_large_tree():
        values = list(range(500))
        random.shuffle(values)
        return BinaryTree.from_iterable(values)

    benchmark(build_large_tree)
