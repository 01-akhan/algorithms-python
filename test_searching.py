from src.searching import linear_search, binary_search

def test_linear_search_found():
    assert linear_search([3,1,4], 1) == 1

def test_linear_search_not_found():
    assert linear_search([1,2,3], 5) is None

def test_binary_search():
    arr = [1,2,3,4,5,6]
    assert binary_search(arr, 4) == 3
    assert binary_search(arr, 7) is None