import logging
import math

logging.basicConfig(level=logging.DEBUG)

# Problem 4. find the largest palindrome product of 2 n digit numbers
# 1. multiply 999 * 999
# 2. work out if number is a palindrome
# 2. if it is store it in array
# 3. find largest


def is_palindrome(number):
    reversed = 0
    temp = number
    while (temp > 0):
        last_digit = temp % 10
        reversed = int(reversed * 10 + last_digit)
        temp = int(temp // 10)
    return number == reversed


def largest_palindrome(n):
    return helper(n)


def helper(n):
    largest_number = int(math.pow(10, n) - 1)
    smallest_number = int(math.pow(10, (n - 1)))
    largest_palindrome = 0
    for outer_number in range(largest_number, smallest_number, -1):
        for inner_number in range(outer_number, smallest_number, -1):
            number = int(outer_number * inner_number)
            if is_palindrome(number) and number > largest_palindrome:
                largest_palindrome = number
                if inner_number > smallest_number:
                    smallest_number = inner_number
                break
    return largest_palindrome


logging.debug("Problem 4. find the largest palindrome product of 2 4 digit numbers is %s", largest_palindrome(4))
