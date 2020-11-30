import logging
import math

logging.basicConfig(level=logging.DEBUG)

# Problem 2. Even Fibonacci numbers
# By considering the terms in the Fibonacci
# sequence whose values do not exceed four million
# find the sum of the even valued terms

# find fibonacci number for 1st odd
# find fibonacci number for 2nd odd
# add the two terms
# save the even fibonacci numbers below 4000000
# sum the even fibonacci numbers

def even_fibonacci(max_value):
    sum = 0
    first_odd = 1
    second_odd = 1
    even_fibonacci = first_odd + second_odd
    while even_fibonacci < max_value:
        sum += even_fibonacci
        first_odd = even_fibonacci + second_odd
        second_odd = even_fibonacci + first_odd
        even_fibonacci = first_odd + second_odd
    return sum


logging.debug(
    "2. The sum of the even valued fibonacci numbers in the sequence whose value does not exceed four million is %s",
    even_fibonacci(4_000_000))