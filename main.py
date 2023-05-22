# LANA CAZANDRA U. LEGASPI - BSCPE 1-5
# CALCULATOR USING OOP CONCEPT

from user_interface import UserInterface
from calculator import Calculator

# pseudocode
user_int = UserInterface()
calcu = Calculator()

# ask for input
# input 1
inp_num1 = user_int.input_num()
# input 2
inp_num2 = user_int.input_num()

# ask for operation
inp_operation = user_int.ask_operation()

# using the add function
if inp_operation == "+":
    sum = calcu.add_input (inp_num1, inp_num2)
    user_int.add_output(sum)

# using the subtract function
elif inp_operation == "-":
    diff = calcu.subtract_input (inp_num1, inp_num2)
    user_int.add_output(diff)

# using the multiply function
elif inp_operation == "*":
    product = calcu.multiply_input (inp_num1, inp_num2)
    user_int.add_output(product)

# using the division function
# add try and except/limitations
# show output
    
else:
    print ("INVALID OPERATION")