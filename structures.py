from collections import deque
from typing import Generic, TypeVar, Optional

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._data: list[T] = []

    def push(self, x: T) -> None:
        self._data.append(x)

    def pop(self) -> T:
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> Optional[T]:
        return self._data[-1] if self._data else None

    def is_empty(self) -> bool:
        return not self._data

class Queue(Generic[T]):
    def __init__(self) -> None:
        self._data: deque[T] = deque()

    def enqueue(self, x: T) -> None:
        self._data.append(x)

    def dequeue(self) -> T:
        if not self._data:
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def is_empty(self) -> bool:
        return not self._data