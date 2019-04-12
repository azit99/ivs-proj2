import re
import math_lib as math

# @file expresion_eval.py
# @author Adam Žitňanský

## @package expresion_eval
# @brief This package evaluates expresions given as strings


## Evaluates the given string expression with the correct operations precedence
    # @param input the string to be evaluated
    # @return the definitive value of the string expresion or errror message
def EvaluateStrExp(input):
    input = prepString(input)

    operationsRgx =[
        "(-*\d+\.?\d*)([\\' \!\ \'])", #factorial
        "(-*\d+\.?\d*)([\\' \^\ \√\  \'])(-*\d+\.?\d*)", #first precedence (pow, root)
        "(-*\d+\.?\d*)([\\' \×\ \÷\ \%\ '])(-*\d+\.?\d*)", #second precedence (*, /,)
        "(-*\d+\.?\d*)([\\' \+\  \-\'])(-*\d+\.?\d*)" # 3rd precedence (+, -)
    ]

    for operationRgx in operationsRgx:
        # loop evalueating every sub-expresion from current grup
        match = re.search (operationRgx, input)
        while match is not None:

            if len(match.groups()) == 3:
                #sub exp has binary operation
                partialRes = repr(calcBinary(float(match.group(1)), float(match.group(3)), match.group(2)))
            else:
                # sub exp has unary operation
                partialRes = repr(calcUnary(float(match.group(1)), match.group(2)))

            # substitution of current sub expr. with it's value
            input = re.sub(operationRgx, partialRes , input, 1)

            #look for another sub expr
            match = re.search(operationRgx,input)
    return input

def calcBinary(a,b,operator):
    if operator == "+":
        return math.add(a,b)
    elif operator == "-":
        return math.sub(a,b)
    elif operator == "×":
        return math.mul(a,b)
    elif operator == "÷":
        try:
            return math.div(a,b)
        except Exception as e:
             return e
    elif operator == "√":
        try:
            return math.root(b,a)
        except Exception as e:
             return e
    elif operator == "^":
        try:
            return math.pow(a,b)
        except Exception as e:
             return e
    elif operator == "%":
        try:
            return math.div(a,b)
        except Exception as e:
             return e

def calcUnary(a,operator):
    if operator == "!":
        try:
            return math.fact(a)
        except Exception as e:
             return e

def prepString(input):
    input=input.replace("−", "-")  #replace minus character from gui with oficial one to avoid conversion problems
    input=input.replace("--", "+") #repalce double minus with plus
    return input