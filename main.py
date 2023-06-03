# LANA CAZANDRA U. LEGASPI - BSCPE 1-5
# CALCULATOR USING OOP CONCEPT

from colorama import init, Fore, Back, Style
init()
import time

from user_interface import UserInterface
from calculator import Calculator
from inherit_calc import InheritCalc

# pseudocode
user_int = UserInterface()
calcu = Calculator()
inherit_calc = InheritCalc()

# ask for input
repeat_prog ="y"
while repeat_prog =="y":
    # showing title
    user_int.design()
    time.sleep(2)

    # asking username
    user_int.ask_user()
    time.sleep(1)

    try:    
        # input 1
        inp_num1 = user_int.input_num()
        print ()
        time.sleep(1)

        # input 2
        inp_num2 = user_int.input_num()
        print ()
        time.sleep(1)

    # adding ValueError limitation
    except ValueError:
        print (Fore.RED + "\nAn ERROR has occured! \nStarting from the first input number, enter a float number to proceed" +  Style.RESET_ALL)
        print ()
        continue

    # ask for operation
    inp_operation = user_int.ask_operation()
    time.sleep(1)

    # using the add function
    try:
        if inp_operation == "+":
            sum = calcu.add_input (inp_num1, inp_num2)
            user_int.add_output(sum)
            time.sleep(1)

        # using the subtract function
        elif inp_operation == "-":
            diff = calcu.subtract_input (inp_num1, inp_num2)
            user_int.subtract_output(diff)
            time.sleep(1)

        # using the multiply function
        elif inp_operation == "*":
            product = calcu.multiply_input (inp_num1, inp_num2)
            user_int.multiply_output(product)
            time.sleep(1)

        # using the division function
        elif inp_operation == "/":
            quotient = calcu.divide_input (inp_num1, inp_num2)
            user_int.divide_output(quotient)
            time.sleep(1)

        # using the exponent operation
        elif inp_operation == "**":
            exponent = inherit_calc.exponent_input (inp_num1, inp_num2)
            user_int.exponent_output(exponent)
            time.sleep(1)
        

        else:
            print ("\nINVALID OPERATION! \nChoose only between (+, -, *, /)")
            print ()
            continue
        time.sleep(1)

    # adding ZeroDivisionError limitation
    except ZeroDivisionError:
        print (Fore.RED + "\nAn ERROR has occured! \nYou can't divide a number to zero. \nEnter your 2 input numbers again." +  Style.RESET_ALL)
        print ()
        continue
    time.sleep(1)

    # asking user if they want to try the program again
    repeat_prog = input(Fore.LIGHTRED_EX + "\nNOTE: Strictly enter 'y' in lowercase. Failure to do so will end the program.\n\nDo you want to run the program again(y/n): " + Style.RESET_ALL)
    time.sleep(1)
    
    if repeat_prog == "n":
        print ("\nTHANK YOU!")
        print()