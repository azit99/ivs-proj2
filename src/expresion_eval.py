import re
import math_lib as math

# @file expresion_eval.py
# @author Adam Žitňanský

## @package expresion_eval
# @brief This package evaluates expresions given as strings


## Evaluates the given string expression with the correct operations precedence (with parentheses support)
    # @param input the string to be evaluated
    # @return the definitive value of the string expresion or errror message

def EvaluateStrExp(expresion):
    if TooMuchOperators(expresion):
        return "Invalid Expression"

    expresion = prepString(expresion)

    #check parenthneses
    if not ParenthnesesPaired(expresion):
        return "Parentheses should be paired!"

    #while there is a parenthes in expresion
    while expresion.find("(") != -1  or expresion.find(")")!=-1:
        #Parentheses indexes
        opening =-1
        closing =-1

        for i in range (len(expresion)):
            if expresion[i] == '(':
                 #check if parentheses are in corect order
                if closing != -1:
                    return "Wrong parentheses usage"
                opening=i

            if expresion[i] == ')':
                #check if parentheses are in corect order
                if opening == -1:
                    return "Wrong parentheses usage"
                closing = i

                #check for vslid operators before current subexpr
                if not ParenthesHasOperation(expresion, opening, closing):
                    return "Invalid expression"

                #substitute parentheses content with it's value
                expresion = expresion.replace(expresion[opening:closing+1], EvalSimpleExp(expresion[opening+1:closing]), 1)
                break

    #now its just simple expr. without parentheses so it can be evaluated
    expresion = prepString(expresion)
    output= EvalSimpleExp(expresion)

    #check output before return
    if InvalidOutput(output):
        return "Invalid expression"
    else:
        return output
######################################### Internal functions #################################

## Flowing funtions are just for internal use and shouldn't be called directly when using the module.

## Evaluates value of expresion w/o parenthneses
def EvalSimpleExp(input):

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
            return math.mod(a,b)
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
    input=input.replace("++", "+") #repalce double minus with plus
    return input

#check if there is same amount of opening and closing parentheses
def ParenthnesesPaired(expr):
    if expr.count('(') == expr.count(')'):
        return True
    else:
        return False

def ParenthesHasOperation(expr, begin, end):
    operators="+-%^×÷√"
    #expresion in parenthnrses is on the beginning so no operator before needed
    if begin == 0:
        return True

    if expr[begin-1] == '(':
        return True

    if begin-2 >= 0 and expr[begin-1] == "!" and operators.find(expr[begin-2]) !=-1 :
        return True

    if operators.find(expr[begin-1]) !=-1:
        return True

    return False

def TooMuchOperators(expr):
    if re.search (r'(\+\+\+|\−\−\−|\^\^|\%\%|\×\×|\√\√|\×\×|\÷\÷|\!\!)',expr) is not None :
        return True
def InvalidOutput(output):
    #if there is operator left(+- is okey) expresion was invalid(operator and operands mismatch)
    if re.search (r'(\^|\%|\×|\√|\×|\÷|\!)',output) is not None :
        return True
    return False

############################################## End of file #######################################
