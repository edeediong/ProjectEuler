def fibo_even_sum(number):
    """Function to calculate the even sum of a Fibonacci seqience.

    Args:
        number: int. The number of terms to be calculated.

    Return:
        sum(content): int. The even sum.
    """
    A = 0
    B = 1
    content = []
    for i in range(number):
        C = A + B
        A = B
        B = C
        if C%2 == 0:
            content.append(C)

    return sum(content)

assert fibo_even_sum(10) == 44
assert fibo_even_sum(18) == 3382
assert fibo_even_sum(23) == 60696
assert fibo_even_sum(43) == 350704366
