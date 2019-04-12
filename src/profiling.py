import math_lib as math
# import expresion_eval as expeval

## @file profiling.py
# @author Samuel Dudík
# @brief Program returns sample standard deviation of n numbers (from stdin, separated by commas)
# Created for profiling

input_string = input()
# remove whitespaces and split string into array of numbers
input_string = input_string.replace(" ", "")
numbers = input_string.split(",")
# convert array of input "numbers" from strings to numbers
numbers = list(map(int, numbers))

n = len(numbers)

# (1 / n) * sum(xi, n)
arithmetic_mean = math.mul(math.div(1, n), sum(numbers))

# n * (arithmetic_mean ^ 2)
subtrahend = math.mul(n, math.pow(arithmetic_mean, 2))

# factor = 0
# for number in numbers:
#     factor += math.sub(math.pow(number, 2), subtrahend)

# sum(xi ^ 2)
minuend = 0
for number in numbers:
    minuend += math.pow(number, 2)

factor = minuend - subtrahend

# 1 / (n - 1)
quotient = math.div(1, math.sub(n, 1))

# √(quotient * factor)
standard_deviation = math.root(math.mul(quotient, factor), 2)

print(standard_deviation)
