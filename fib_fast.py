matrix multiplication function
def mat_mul(x: list[int], z: list[int]) -> list[int]:
    return [[x[0][0] * z[0][0] + x[0][1] * z[1][0],
             x[0][0] * z[0][1] + x[0][1] * z[1][1]],
            [x[1][0] * z[0][0] + x[1][1] * z[1][0],
             x[1][0] * x[0][1] + x[1][1] * x[1][1]]]

'''
O(n) Fibonacci number calculator with O(1)
space complexity.
'''
def pure_fib_mat(n: int) -> int`:

    # First step of algorithm
    step = [[0, 1],
            [1, 1]]

    # 2x2 identity matrix
    fib = [[1, 0],
           [0, 1]]

    while n > 0:
        if n & 1:
            fib = mat_mul(fib, step)
        step = mat_mul(step, step)
        n >>= 1
    return fib[0][1]
