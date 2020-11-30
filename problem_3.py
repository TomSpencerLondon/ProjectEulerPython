import logging
import math

logging.basicConfig(level=logging.DEBUG)

# 3. What is the largest prime factor of 600851475143
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