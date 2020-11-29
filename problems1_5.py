import logging
import math

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
    return int(3 * sum_numbers(n / 3) + 5 * sum_numbers(n / 5) - 15 * sum_numbers(n / 15))


def sum_numbers(n):
    return n * (n + 1) // 2


logging.debug("1.(b) Sum of multiples of 3 and 5 below 1000 is %s", sum_multiples_recursion())


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


# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29
# What is the largest prime factor of the number 600851475143

# find primes of 600851475143
# return the highest prime from this list

def get_factors(number):
    factors = []
    for potentialFactor in range(1, int(math.sqrt(number))):
        if number % potentialFactor == 0:
            factors.append(potentialFactor)
            factors.append(number // potentialFactor)
    return factors

def is_prime(input):
    return len(get_factors(input)) == 2



all_factors = get_factors(600_851_475_143)
largest_prime = 0
for factor in all_factors:
    if is_prime(factor) and factor > largest_prime:
        largest_prime = factor

logging.debug("3. The largest prime factor of 600851475143 is %s", largest_prime)
