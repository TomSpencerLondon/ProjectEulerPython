import logging

logging.basicConfig(level=logging.DEBUG)
# Problem 5. Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder
# What is the smallest positive number that is evenly divisible (divisible with no remainder) by all the numbers from
# 1 to 20

# tell if number is divisible by 1 to 20


# starting at number 1, check if it's divisible by all numbers 1 to 20
# increment number

# found number stop

def isDivisibleOneToTwenty(number):
    for i in range(2, 21):
        if number % i != 0:
            return False
    return True

def checkNumbers():
    number = 20
    while True:
        if isDivisibleOneToTwenty(number):
            return number
        number += 20

logging.debug("Problem 5. Smallest multiple of that is divisible by all numbers from 1 - 20 is %s", checkNumbers())