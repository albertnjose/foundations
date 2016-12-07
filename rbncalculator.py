# Reverse Polish Notation Calculator
# 52+ = 5 + 2 = 7
# OOP solution

class calculator():
    """Reverse Polish Notation Calculator"""

# initialize stack to hold values
    def __init__(self, stack=[]):
        self.stack = []
# add values to stack
    def push(self, value):
        self.stack.append(value)
# to print last value in stack
    def value(self):
        return self.stack[len(self.stack) - 1]
# pop method and check if there are no elements left
    def pop(self):
        if len(self.stack) == 0:
            print("Calculator is empty")
            exit()
        else:
            value = self.stack.pop()
            return value
    def add(self):
        self.stack.append(self.pop() + self.pop())

    def multiply(self):
        self.stack.append(self.pop() * self.pop())
# operand order matters for subtraction and division
    def subtract(self):
        second = self.pop()
        first = self.pop()
        self.stack.append(first - second)

    def divide(self):
        second = self.pop()
        first = self.pop()
        self.stack.append(first / second)

if __name__ == "__main__":
    calc = calculator()
    calc.push(6)
    calc.push(2)
    calc.push(3)
    calc.divide()
    print(calc.value())
    calc.add()
    print(calc.value())
