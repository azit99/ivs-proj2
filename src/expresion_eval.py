import re
import math_lib as math

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
        return math.div(a,b)
    elif operator == "√":
        return math.root(b,a)
    elif operator == "^":
        return math.pow(a,b)
    elif operator == "%":
        return math.mod(a,b)

def calcUnary(a,operator):
    if operator == "!":
        return math.fact(a)

def prepString(input):
    input=input.replace("−", "-")
    input=input.replace("--", "+")
    return input
