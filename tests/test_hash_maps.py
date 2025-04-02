import pytest
from nebula.data_structures import HashMap
from typing import Any

# Basic Tests
def test_hashmap_creation():
    hmap = HashMap()
    assert hmap is not None
    assert len(hmap) == 0

def test_hashmap_put():
    hmap = HashMap()
    hmap['key1'] = 'value1'  # tests __setitem__
    assert hmap['key1'] == 'value1'  # tests __getitem__

# Intermediate Tests
def test_hashmap_iterable():
    hmap = HashMap.from_dict({'a': 1, 'b': 2, 'c': 3})
    assert len(hmap) == 3  # tests __len__
    assert list(hmap) == ['a', 'b', 'c']  # tests __iter__
    assert 'b' in hmap  # tests __contains__

def test_hashmap_views():
    hmap = HashMap.from_dict({'a': 1, 'b': 2})
    assert list(hmap.keys()) == ['a', 'b']
    assert list(hmap.values()) == [1, 2]
    assert list(hmap.items()) == [('a', 1), ('b', 2)]

# Advanced Features Tests
def test_hashmap_operations():
    h1 = HashMap.from_dict({'a': 1, 'b': 2})
    h2 = HashMap.from_dict({'c': 3, 'd': 4})
    h3 = h1 + h2  # tests __add__
    assert dict(h3) == {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Performance Tests
@pytest.mark.benchmark
def test_hashmap_large_scale(benchmark):
    def build_large_map():
        return HashMap.from_dict({str(i): i for i in range(10_000)})
    benchmark(build_large_map)
