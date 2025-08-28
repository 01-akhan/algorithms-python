import random, timeit
from src.sorting import bubble_sort, insertion_sort, merge_sort, quick_sort

def bench(fn, n=2000, repeat=3):
    arr = [random.randint(0, 10**6) for _ in range(n)]
    t = timeit.timeit(lambda: fn(arr), number=repeat)
    print(f"{fn.__name__:<15} n={n:>5}  time={t:.3f}s (repeat={repeat})")

if __name__ == "__main__":
    for n in (500, 2000, 8000):
        print(f"\n=== N={n} ===")
        bench(bubble_sort, n)
        bench(insertion_sort, n)
        bench(merge_sort, n)
        bench(quick_sort, n)