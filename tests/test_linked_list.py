import pytest
from nebula.data_structures import LinkedList, Node
from itertools import chain


# Basic Tests
def test_linked_list_init():
    linked_list = LinkedList()
    assert linked_list.head is None
    assert linked_list.tail is None
    assert linked_list.size == 0


def test_linked_list_append_basic():
    ll = LinkedList()
    ll.append(1)
    assert ll.head.value == 1
    assert ll.tail.value == 1
    assert ll.size == 1


def test_linked_list_append():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    assert linked_list.size == 3
    values = [node.value for node in linked_list.traverse()]
    assert values == [1, 2, 3]


# Intermediate Tests
def test_linked_list_iterable():
    ll = LinkedList.from_iterable([1, 2, 3])
    assert list(ll) == [1, 2, 3]  # tests __iter__
    assert len(ll) == 3  # tests __len__
    assert bool(ll) is True  # tests __bool__
    assert bool(LinkedList()) is False


def test_linked_list_reversible():
    ll = LinkedList([1, 2, 3])
    assert list(reversed(ll)) == [3, 2, 1]  # tests __reversed__


def test_linked_list_containment():
    ll = LinkedList([1, 2, 3])
    assert 2 in ll  # tests __contains__
    assert 5 not in ll


def test_linked_list_init_with_iter():
    linked_list = LinkedList.from_iterable([1, 2, 3, 4, 5])
    assert linked_list.size == 5
    values = [node.value for node in linked_list.traverse()]
    assert values == [1, 2, 3, 4, 5]


def test_linked_list_init_with_head():
    head = Node(1)
    head.next = Node(2)
    linked_list = LinkedList.from_node(head)
    assert linked_list.size == 2
    values = [node.value for node in linked_list.traverse()]
    assert values == [1, 2]


def test_linked_list_str():
    linked_list = LinkedList.from_iterable([1, 2, 3, 4, 5])
    assert str(linked_list) == "[ 1 ] -> [ 2 ] -> [ 3 ] -> [ 4 ] -> [ 5 ]"


def test_linked_list_delete():
    linked_list = LinkedList.from_iterable([1, 2, 3, 4, 5])
    linked_list.delete(3)
    assert linked_list.size == 4
    values = [node.value for node in linked_list.traverse()]
    assert values == [1, 2, 4, 5]


def test_linked_list_traverse():
    linked_list = LinkedList.from_iterable([1, 2, 3, 4, 5])
    values = [node.value for node in linked_list.traverse()]
    assert values == [1, 2, 3, 4, 5]


def test_linked_list_addition():
    linked_list1 = LinkedList.from_iterable([1, 2, 3, 4, 5])
    linked_list2 = LinkedList.from_iterable([-10, 12, 0])
    linked_list3 = linked_list1 + linked_list2
    assert linked_list3.size == 8
    values = [node.value for node in linked_list3.traverse()]
    assert values == [1, 2, 3, 4, 5, -10, 12, 0]


# Advanced Features Tests
def test_linked_list_slicing():
    ll = LinkedList(range(10))
    assert list(ll[2:5]) == [2, 3, 4]  # tests __getitem__
    assert list(ll[::2]) == [0, 2, 4, 6, 8]


def test_linked_list_arithmetic():
    ll1 = LinkedList([1, 2])
    ll2 = LinkedList([3, 4])
    ll3 = ll1 + ll2  # tests __add__
    assert list(ll3) == [1, 2, 3, 4]

    ll4 = ll1 * 2  # tests __mul__
    assert list(ll4) == [1, 2, 1, 2]


# Performance Tests
def test_linked_list_large_scale():
    @pytest.mark.benchmark
    def test_append_performance(benchmark):
        def append_items():
            ll = LinkedList()
            for i in range(10_000):
                ll.append(i)

        benchmark(append_items)


# Edge Cases and Complex Operations
def test_linked_list_complex_operations():
    ll1 = LinkedList.from_iterable([1, 2, 3])
    ll2 = LinkedList.from_iterable([4, 5, 6])

    # Test chain operations
    ll3 = LinkedList.from_iterable(chain(ll1, ll2, ll1))
    assert list(ll3) == [1, 2, 3, 4, 5, 6, 1, 2, 3]

    # Test nested structures
    nested = LinkedList.from_iterable([ll1, ll2])
    assert len(nested) == 2
    assert isinstance(nested.head.value, LinkedList)


# Comparison Tests
def test_linked_list_comparison():
    ll1 = LinkedList([1, 2, 3])
    ll2 = LinkedList([1, 2, 3])
    ll3 = LinkedList([1, 2, 4])

    assert ll1 == ll2  # tests __eq__
    assert ll1 != ll3
    assert ll1 < ll3  # tests __lt__
    assert ll3 > ll1  # tests __gt__
