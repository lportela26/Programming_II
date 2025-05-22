from typing import Callable

def my_decorator(func: Callable) -> Callable:
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello!")

greet()


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(4)
def greet():
    print("hello")

greet()

def repeat_and_print(n: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("Before the func")
            for i in range(n):
                func(*args, **kwargs)
            print("Afterrrr")
        return wrapper
    return decorator

@repeat_and_print(4)
def greet():
    print("hello")

greet()