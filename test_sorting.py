from src.sorting import bubble_sort, insertion_sort, merge_sort, quick_sort

def _check_sorted(func):
    data = [5,3,8,1,2,7]
    assert func(data) == sorted(data)

def test_bubble(): _check_sorted(bubble_sort)
def test_insertion(): _check_sorted(insertion_sort)
def test_merge(): _check_sorted(merge_sort)
def test_quick(): _check_sorted(quick_sort)