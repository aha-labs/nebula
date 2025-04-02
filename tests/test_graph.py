import pytest
from nebula.data_structures import Graph
from typing import Any
from itertools import chain

# Basic Tests
def test_graph_creation():
    graph = Graph()
    assert graph is not None
    assert len(graph) == 0

def test_graph_add_vertex():
    graph = Graph()
    graph.add_vertex('A')
    assert 'A' in graph

# Intermediate Tests
def test_graph_iterable():
    graph = Graph.from_edges([('A', 'B'), ('B', 'C')])
    assert list(graph) == ['A', 'B', 'C']  # tests __iter__
    assert len(graph) == 3  # tests __len__
    assert 'A' in graph  # tests __contains__

def test_graph_item_access():
    graph = Graph.from_edges([('A', 'B'), ('B', 'C')])
    assert graph['A'] == ['B']  # tests __getitem__
    
    graph['D'] = ['A']  # tests __setitem__
    assert 'D' in graph
    assert 'A' in graph['D']

# Advanced Features Tests
def test_graph_operations():
    g1 = Graph.from_edges([('A', 'B')])
    g2 = Graph.from_edges([('B', 'C')])
    g3 = g1 + g2  # tests __add__
    assert list(g3.edges()) == [('A', 'B'), ('B', 'C')]

def test_graph_representation():
    graph = Graph.from_edges([('A', 'B'), ('B', 'C')])
    assert str(graph) == "A -> B\nB -> C"  # tests __str__
    assert eval(repr(graph)) == graph  # tests __repr__

# Performance Tests
@pytest.mark.benchmark
def test_graph_large_scale(benchmark):
    def create_large_graph():
        g = Graph()
        for i in range(1000):
            g.add_vertex(i)
            if i > 0:
                g.add_edge(i-1, i)
    benchmark(create_large_graph)
