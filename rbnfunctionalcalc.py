# Reverse Polish Notion Calculator
# Input from user
# Parse input, operands in stack and run operators
# loop through and show result

import math
import operator

# ops dictionary

ops = { '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '^': operator.pow,
        'sin': math.sin,
        'tan': math.tan,
        'cos': math.cos,
        'pi': math.pi }

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

def calculate(equation):
    stack = []
    result = 0

    for i in equation:
        if is_number(i):
            stack.insert(0, float(i))
        else:
            if len(stack) < 2:
                print("Not enough values")
                break
            else:
                print('Stack: {}'.format(stack))
                if(len(i) == 1):
                    n1 = stack.pop(1)
                    n2 = stack.pop(0)
                    result = ops[i](n1, n2)
                    stack.insert(0, result)
                else:
                    n1 = stack.pop(0)
                    result = ops[i](math.radians(n1))
                    stack.insert(0, result)

    return result

def main():
    equation = input('Enter equation with spaces: ').split(' ')
    answer = calculate(equation)
    print('Result: {}'.format(answer))

if __name__ == '__main__':
    main()
