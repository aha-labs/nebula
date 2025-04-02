import pytest
from nebula.data_structures import Heap
from typing import Any

# Basic Tests
def test_heap_creation():
    heap = Heap()
    assert heap is not None
    assert len(heap) == 0

def test_heap_push():
    heap = Heap()
    heap.push(5)
    assert heap.peek() == 5

# Intermediate Tests
def test_heap_iterable():
    heap = Heap.from_iterable([3, 1, 4, 1, 5])
    assert list(heap) == [1, 1, 3, 4, 5]  # tests __iter__
    assert len(heap) == 5  # tests __len__
    assert bool(heap) is True  # tests __bool__

def test_heap_comparison():
    heap = Heap.from_iterable([3, 1, 4])
    assert 1 in heap  # tests __contains__
    assert heap[0] == 1  # tests __getitem__

# Advanced Features Tests
def test_heap_operations():
    h1 = Heap.from_iterable([1, 3, 5])
    h2 = Heap.from_iterable([2, 4, 6])
    h3 = h1 + h2  # tests __add__
    # should construct a new heap with all elements
    assert list(h3) == [1, 2, 3, 4, 5, 6]

# Performance Tests
@pytest.mark.benchmark
def test_heap_large_scale(benchmark):
    def heapify_large():
        return Heap.from_iterable(range(10_000))
    benchmark(heapify_large)
