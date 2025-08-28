from src.structures import Stack, Queue

def test_stack_basic():
    s = Stack[int]()
    s.push(1); s.push(2)
    assert s.peek() == 2
    assert s.pop() == 2
    assert s.pop() == 1

def test_queue_basic():
    q = Queue[int]()
    q.enqueue(1); q.enqueue(2)
    assert q.dequeue() == 1
    assert q.dequeue() == 2