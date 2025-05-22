import timeit
from functools import wraps
import time

duration = timeit.timeit("sum([i**2 for i in range(100_000)])", number=10)
print(f"Average time over 10 runs: {duration/10:.2f} seconds")

def timing(func):
    @wraps(func)  
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start

        print(f"Function {func.__name__} called with args: {args}, kwargs: {kwargs} -- took {duration:.4f} s")

        return result
    return wrapper


@timing
def slow_add(x, y):
    time.sleep(1)
    return x + y

slow_add(3, 9)


def scheduler(seconds=1):
    start = time.time()
    while True:
        time.sleep(seconds)
        yield time.time() - start

for t in scheduler(seconds=1):
    print(f"{t:.2f} seconds")
    if t > 5:
        break

