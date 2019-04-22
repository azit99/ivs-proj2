import re
import math_lib as math

## @brief This module is buid to evaluate calculator input
# @file expresion_eval.py
# @author Adam Žitňanský

## @package expression_evaluation
# @brief This module evaluates string expressions
# @details The module supports expressions with support of parentnesses
# and operations precedence

## Evaluates expression \b expression
# @param expression string expression to be evaluated
# @return value of the expression
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

 #Internal functions
# Flowing funtions are just for internal use and shouldn't be called directly when using the module.

## Evaluates value of expresion w/o parenthneses
# @param input Expression w/o parentnesses to be evalueated
# @return Value of the expression
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

## Call math library function based on operator (for binary operators)
# @param a First operand
# @param b Second operand
# @param operator Operator character
# @return result of the operation
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

## Call math library function based on operator (for unary operators)
# @param a First and only operand
# @param operator Operator character
# @return result of the operation
def calcUnary(a,operator):
    if operator == "!":
        try:
            return math.fact(a)
        except Exception as e:
             return e

## Prepares string for evaluating method
# @param iput Expression which need to be prepared
# @return expression ready for evaluation
def prepString(input):
    input=input.replace("−", "-")  #replace minus character from gui with oficial one to avoid conversion problems
    input=input.replace("--", "+") #repalce double minus with plus
    input=input.replace("++", "+") #repalce double minus with plus
    return input

##Check if there is same amount of opening and closing parentheses
# @param expr Expresion to check for corect parentnesses
# @return True if parentnesses are paired, False if they aren't
def ParenthnesesPaired(expr):
    if expr.count('(') == expr.count(')'):
        return True
    else:
        return False

##Check if parentnesses are conected with correct operators
# @param expr Expression to be chacked
# @param begin index of currently evaluated opening perentness
# @param end index of currently evaluated closing parentness
# @return true if is correctly conected with operators else false
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

##Check if expression contains too much operators
# @param expr Expression to be chacked
# @return True if has too much operators else false
def TooMuchOperators(expr):
    if re.search (r'(\+\+\+|\−\−\−|\^\^|\%\%|\×\×|\√\√|\×\×|\÷\÷|\!\!)',expr) is not None :
        return True

##checks if there is operator left in output what indictes wrong nuber of operands
# @param output Output to be checked
# @return true if there is operator left else false
def InvalidOutput(output):
    #if there is operator left(+- is okey) expresion was invalid(operator and operands mismatch)
    if re.search (r'(\^|\%|\×|\√|\×|\÷|\!)',output) is not None :
        return True
    return False

# End of file
