#!/usr/bin/python3

class Calculator:
    __result = 0

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def calculate(self, operator):
        if operator == "+":
            self.__result = self.num1 + self.num2
        elif operator == "-":
            self.__result = self.num1 - self.num2
        elif operator == "*":
            self.__result = self.num1 * self.num2
        elif operator == "/":
            self.__result = self.num1 / self.num2
        else:
            print("Unknown operator")

    def getResult(self):
        return self.__result

calc = Calculator(5,6)
calc.calculate("+")
print('Result :', calc.getResult())
calc.calculate("-")
print('Result :', calc.getResult())
