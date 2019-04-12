from expresion_eval import EvaluateStrExp as evalexp

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

# (1 / n) * sum(xi)
arithmetic_mean = evalexp("1÷{}×{}".format(str(n), sum(numbers)))

# n * (arithmetic_mean ^ 2)
subtrahend = evalexp("{}×{}^2".format(n, arithmetic_mean))

# sum(xi ^ 2)
minuend = 0
for number in numbers:
    minuend += float(evalexp("{}^2".format(number)))

factor = evalexp("{}-{}".format(minuend, subtrahend))

# 1 / (n - 1)
quotient = evalexp("1÷{}".format(evalexp("{}-1".format(n))))

# √(quotient * factor)
standard_deviation = evalexp("2√{}".format(evalexp("{}×{}".format(quotient, factor))))

print(standard_deviation)
