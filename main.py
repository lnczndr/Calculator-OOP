# LANA CAZANDRA U. LEGASPI - BSCPE 1-5
# CALCULATOR USING OOP CONCEPT

from user_interface import UserInterface
from calculator import Calculator

# pseudocode
user_int = UserInterface()
calcu = Calculator()

# ask for input
repeat_prog ="y"
while repeat_prog =="y":

    try:
        # asking username
        user_int.ask_user()

        # input 1
        inp_num1 = user_int.input_num()
        print ()

        # input 2
        inp_num2 = user_int.input_num()
        print ()

    # adding ValueError limitation
    except ValueError:
        print ("\nAn ERROR has occured! \nStarting from the first input number, enter a float number to proceed")
        print ()
        continue

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

        else:
            print ("\nINVALID OPERATION! \nChoose only between (+, -, *, /)")
            print ()
            continue

    # adding ZeroDivisionError limitation
    except ZeroDivisionError:
        print ("\nAn ERROR has occured! \nYou can't divide a number to zero. \nEnter your 2 input numbers again.")
        print ()
        continue

    # asking user if they want to try the program again
    repeat_prog = input("\nNOTE: Strictly enter 'y' in lowercase. Failure to do so will end the program.\n\nDo you want to run the program again(y/n): ")

    if repeat_prog == "n":
        print ("\nTHANK YOU!")
        print()