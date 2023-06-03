# LANA CAZANDRA U. LEGASPI - BSCPE 1-5
# OOP - Calculator Inheritance

# import calculator.py
from calculator import Calculator

# make a new class
class InheritCalc(Calculator):

# inherit the calculator.py
    def __init__(self):
        super().__init__()

# additional operations

    def exponent_input (self, inp_num1, inp_num2):
        exponent = inp_num1 ** inp_num2
        return exponent

    def remainder_input(self, inp_num1, inp_num2):
        remainder = inp_num1 % inp_num2
        return remainder