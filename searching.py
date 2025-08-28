from typing import List, Optional

def linear_search(arr: List[int], target: int) -> Optional[int]:
    """Return index of target in arr or None if not found. O(n)."""
    for i, x in enumerate(arr):
        if x == target:
            return i
    return None

def binary_search(arr: List[int], target: int) -> Optional[int]:
    """Binary search in a **sorted** array. O(log n)."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None