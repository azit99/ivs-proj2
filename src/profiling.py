from expresion_eval import EvaluateStrExp as evalexp
import random

## @file profiling.py
# @author Samuel Dudík
# @brief Program returns sample standard deviation of n numbers (from stdin, separated by commas)
# Created for profiling

# False = expects input on stdin; True = will randomly generate input based on the rest of settings
profiling = False
# number of randomly generated numbers used as input
profiling_amount = 10
# upper and lower limit for randomly generated numbers
profiling_lower = 1
profiling_upper = 1000

numbers = []

if profiling:
    for _ in range(profiling_amount):
        numbers.append(random.randint(profiling_lower, profiling_upper))
else:
    input_string = input()
    # remove whitespaces and split string into array of numbers
    input_string = input_string.replace(" ", "")
    numbers = input_string.split(",")
    # convert array of input "numbers" from strings to numbers
    numbers = list(map(int, numbers))

n = len(numbers)

# (1 / n) * sum(xi)
arithmetic_mean = evalexp("1÷{}×{}".format(n, sum(numbers)))

# sum(xi ^ 2)
minuend = 0
for number in numbers:
    minuend += float(evalexp("{}^2".format(number)))

standard_deviation = evalexp("2√(1÷({}-1)×({}-{}×{}^2))".format(n, minuend, n, arithmetic_mean))

print(standard_deviation)
