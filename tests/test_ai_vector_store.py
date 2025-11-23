import pytest
from bayan.libraries.vector_store_lib import create_collection, add_documents, search

def test_vector_store_basic():
    name = create_collection("test_store")
    assert name == "test_store"
    
    docs = ["apple", "banana", "cherry"]
    # Dummy embeddings: 2D
    embeddings = [[1.0, 0.0], [0.9, 0.1], [0.0, 1.0]]
    
    add_documents(name, docs, embeddings)
    
    # Query close to apple/banana
    results = search(name, [1.0, 0.0], k=2)
    
    assert len(results) == 2
    assert results[0]['doc'] == "apple"
    assert results[1]['doc'] == "banana"

def test_vector_store_empty():
    name = create_collection("empty_store")
    results = search(name, [1.0, 0.0])
    assert len(results) == 0
