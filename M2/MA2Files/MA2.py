"""
Solutions to module 2 - A calculator
Student: Oliver Groth
Mail: oliver.groth.7974@student.uu.se
Reviewed by: Julia
Reviewed date: 25 April
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

import math
from tokenize import TokenError  
from MA2tokenizer import TokenizeWrapper


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


def statement(wtok, variables):
    if wtok.is_at_end():
        return
    else:
        result = assignment(wtok, variables)
        if wtok.is_at_end():
            return result
        else:
            raise SyntaxError("Expected EOL")

def assignment(wtok, variables):
    """ See syntax chart for assignment"""
    result = expression(wtok, variables)
    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
            variables[wtok.get_current()] = result
            wtok.next()
        else:
            raise SyntaxError("Trying to assign non-name")
    return result

def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    while wtok.get_current() == '+' or wtok.get_current() == '-':
        if wtok.get_current() == '+':
            wtok.next()
            result = result + term(wtok, variables)
        elif wtok.get_current() == '-':
            wtok.next()
            result = result - term(wtok, variables)
    return result


def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    while wtok.get_current() == '*' or wtok.get_current() == '/': 
        if wtok.get_current() == '*':
            wtok.next()
            result = result * factor(wtok, variables)
        elif wtok.get_current() == '/':
            wtok.next()
            denominator = factor(wtok, variables)
            if denominator == 0:
                raise EvaluationError("Division with zero")
            else:
                result = result / denominator


        #elif wtok.get_current() == '/':
        #    print("delat")
        #    wtok.next()
        #    if factor(wtok, variables) == 0:
        #        raise EvaluationError("Division with zero")
        #    result = result / factor(wtok, variables)
    return result

def arglist(wtok, variables):
    result = []
    if wtok.get_current() == '(':
        wtok.next()
        while True:
            result.append(assignment(wtok, variables))
            if wtok.get_current() == ')':
                wtok.next()
                return result
            elif wtok.get_current() == ',':
                wtok.next()
            else:
                raise SyntaxError("Expected ')' or ','")
    else:
        raise SyntaxError("Expected '('")
    return result


def factor(wtok, variables):
    """ See syntax chart for factor"""
    # I really don't like the idea of putting the dictionarys here
    functions_1 = {"sin": sin, "cos": cos, "exp": exp, "log": log, "fib": fib, "fac": fac}
    functions_n = {"sum": sum, "max": max, "min": min, "mean": mean}

    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()

    elif wtok.get_current() in functions_1:
        func = wtok.get_current()
        wtok.next()
        if wtok.get_current() != '(':
            raise SyntaxError("Expected '('")
        result = functions_1[func](factor(wtok, variables))

    elif wtok.get_current() in functions_n:
        func = wtok.get_current()
        wtok.next()
        result = functions_n[func](arglist(wtok, variables))
        

    elif wtok.is_name():
        if wtok.get_current() in variables:
            result = variables[wtok.get_current()]
            wtok.next()
        else:
            raise EvaluationError("Undefined variable: " + wtok.get_current())
            
    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()

    elif wtok.get_current() == '-':
        wtok.next()
        result = -1 * factor(wtok, variables)

    else:
        raise SyntaxError(
            "Expected number or '('")  
    return result

# FUNCTIONS

def sin(x):
    result = math.sin(float(x))
    return result

def cos(x):
    result = math.cos(float(x))
    return result

def exp(x):
    return math.exp(float(x))

def log(x):
    if float(x) > 0:
        return math.log(float(x))
    else:
        raise EvaluationError("Domain error")

def fib(x):
    if x < 0:
        raise EvaluationError("fib requiers positive int")
    elif float(x).is_integer():
        x = int(x)
        if x == 0:
            result = 0
        else:
            sequence = [0]*(x+1)
            sequence[1] = 1
            for i in range(2,x+1):
                sequence[i] = sequence[i-1] + sequence[i-2]
            result = sequence[-1]
    else:
        raise EvaluationError("fib requiers int")
    return result

def fac(x):
    if x < 0:
        raise EvaluationError("fac requires positive values")
    elif float(x).is_integer():
        x = int(x)
        return math.factorial(x)
    else:
        raise EvaluationError("fac requiers int")

def mean(wtok):
    return sum(wtok) / len(wtok)
         
def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """
    
    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    #functions_1 = {"sin": sin, "cos": cos, "exp": exp, "log": log, "fib": fib, "fac": fac}
    #functions_n = {"sum": sum, "max": max, "min": min, "mean": mean}
    init_file = 'MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0]=='#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        elif wtok.get_current() == 'vars':
            print(variables)
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except EvaluationError as ee:
                print("*** Evaluation error: ", ee)

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')
 


if __name__ == "__main__":
    main()
