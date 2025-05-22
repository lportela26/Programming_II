from numba import njit

@njit
def square_sum(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

