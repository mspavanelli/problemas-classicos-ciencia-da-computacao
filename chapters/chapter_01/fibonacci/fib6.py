from typing import Generator

def fib6(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0: yield 1
    last: int = 0
    current: int = 1
    for _ in range(1, n):
        last, current = current, current + last
        yield current

for i in fib6(20):
    print(i, end=' ')