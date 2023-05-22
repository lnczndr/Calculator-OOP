# LANA CAZANDRA U. LEGASPI - BSCPE 1-5
# CALCULATOR USING OOP CONCEPT

from user_interface import UserInterface
from calculator import Calculator

# pseudocode
user_int = UserInterface()
calcu = Calculator()

# ask for input
try:
    # input 1
    inp_num1 = user_int.input_num()
    # input 2
    inp_num2 = user_int.input_num()

# adding ValueError limitation
except ValueError:
    print ("An ERROR has occured! \nYou need to input float numbers.")

# ask for operation
inp_operation = user_int.ask_operation()

# using the add function
try:
    if inp_operation == "+":
        sum = calcu.add_input (inp_num1, inp_num2)
        user_int.add_output(sum)

    # using the subtract function
    elif inp_operation == "-":
        diff = calcu.subtract_input (inp_num1, inp_num2)
        user_int.subtract_output(diff)

    # using the multiply function
    elif inp_operation == "*":
        product = calcu.multiply_input (inp_num1, inp_num2)
        user_int.multiply_output(product)

    # using the division function
    elif inp_operation == "/":
        quotient = calcu.divide_input (inp_num1, inp_num2)
        user_int.divide_output(quotient)

# adding ZeroDivisionError limitation
except ZeroDivisionError:
    print ("An ERROR has occured! \nYou can't divide a number to zero.")

# show output
    
else:
    print ("INVALID OPERATION")