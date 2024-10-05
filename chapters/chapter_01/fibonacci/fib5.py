def fib5(n: int) -> int:
    if n == 0:
        return 0
    last: int = 0
    current: int = 1
    for _ in range(1, n):
        last, current = current, current + last
    return current
