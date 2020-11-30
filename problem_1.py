import logging

logging.basicConfig(level=logging.DEBUG)


# Problem 1: Find the sum of all the multiples of 3 or 5 below 1000
# find multiples of 3 or 5 below 1000
# add the multiples together

def sumMultiples():
    sum = 0
    for number in range(1, 1000):
        if (number % 3 == 0) or (number % 5 == 0):
            sum += number
    return sum


result = sumMultiples()
logging.debug("1. Sum of multiples of 3 and 5 below 1000 is %s", result)


def sum_multiples_recursion():
    n = 1000
    n -= 1
    return int(3 * sum_numbers(n // 3) + 5 * sum_numbers(n // 5) - 15 * sum_numbers(n // 15))


def sum_numbers(n):
    return n * (n + 1) // 2


logging.debug("1.(b) Sum of multiples of 3 and 5 below 1000 is %s", sum_multiples_recursion())
