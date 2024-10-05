from functools import lru_cache

@lru_cache(maxsize=None)
def fib2(n: int) -> int:
    if n < 2:
        return 1
    return fib2(n - 1) + fib2(n - 2)
