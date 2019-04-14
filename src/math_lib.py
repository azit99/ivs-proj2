"""
=======================================================================================

        Filename:  math_lib.py

     Description: This is a basic arithemtic library meant for simple operations that
                  wil be used in calculator. The code uses Python3 language and briefly
                  generates some short and simple documentation in Doxygen.


         Version:  1.0
         Created:  30.03.2019 14:31:35
        Revision:  none

          Author:  MATEJ OTCENAS
=======================================================================================

"""
import math
import traceback

## @brief Documentation for math library
# @file math_lib.py
# @author Matej Otcenas

## @class Math_Library
# @brief This mathematic class contains basic arithmetic operations
# @details The list of operations is here: addition, substraction, multiplying, dividing,
# factorial, squaring, modulo, absolute value


    ## Adds two numbers \b a , \b b
    # @param a first number
    # @param b second number
    # @return addition of two numbers
def add(a, b):
    return a + b


    ## Substracts two numbers \b a , \b b
    # @param a first number
    # @param b second number
    # @return substraction of two numbers
def sub(a, b):
    return a - b


    ## Multiplies two numbers \b a , \b b
    # @param a first number
    # @param b second number
    # @return multiplication of two numbers
def mul(a, b):
    return a * b


    ## Divides two numbers \b a , \b b
    # @param a first number
    # @param b second number
    # @return division of two numbers \b a / \b b or \a None if second number is 0
def div(a, b):
    try:
        return float(a) / float(b)
    except:
        raise


    ## Does a factorial
    # @param a first and only number
    # @return factorial of number \b a or \a None if number is negative
def fact(a):
    if isinstance(a, float):
        if a.is_integer():
            a=int(a)
        else:
            raise ValueError
    try:
        if a < 0:
            raise ValueError
        else:
            a=int(a)
            factorial = 1
            for i in range(1, a + 1):
                factorial = factorial * i
            return factorial
    except:
        raise


    ## Squares number \b a to \b e
    # @param a first number
    # @param e second number
    # @return squared number \b a or \a None if second number is negative
def pow(a, e):
    try:
        if e == 0 and a == 0:
            raise ValueError

        elif e == 0:
            return 1

        elif e == 1:
            return a

        elif e < 0:
            raise ValueError

        else:
            return float (a ** int(e))
    except:
        raise


    ## Squares number \b a to \b 2
    # @param a first and only number
    # @return squared number \b a
def pow2(a):
    return a ** 2


    ## Squares number \b a to \b 3
    # @param a first and only number
    # @return squared number \b a
def pow3(a):
    return a ** 3


    ## Squares root of number \b a
    # @param a first number
    # @param b second number
    # @return squared to root number \b a or \a None if number is negative
def root(a, b):
    if a >= 0 and b != 0:
        return a**(b**(-1))
    else:
        raise ValueError


    ## Negates number \b a
    # @param a first and only number
    # @return negated number \b a
def negative(a):
    return -a


    ## Does modulo of numbers \b a \a mod \b b
    # @param a first number
    # @param b second number
    # @return remainder of number \b a or \a None if second number is 0
def mod(a, b):
    if b == 0:
        return None
    else:
        return a % b


    ## Does absolute value of number \b a
    # @param a first and only number
    # @return absolute value of number \b a
def abs(a):
    if a < 0:
        return -a
    else:
        return a
