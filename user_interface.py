# LANA CAZANDRA U. LEGASPI - BSCPE 1-5
# CALCULATOR USING OOP CONCEPT

# pseudocode
# creating class for "UserInterface" 
from colorama import init, Fore, Back, Style
init()

class UserInterface:
    
# ask for input
    def input_num (self):
        inp_num = float(input(Fore.CYAN + "ENTER NUMBER: " + Style.RESET_ALL))
        return inp_num
    
# ask for operation
    def ask_operation (self):
        operation = (input(Fore.YELLOW + "ENTER OPERATION (+, -, *, /): " + Style.RESET_ALL))
        return operation
    
# show output for addition
    def add_output (self, sum):
        print (Fore.MAGENTA + "\nANSWER: ", str(sum) + Style.RESET_ALL)
    
# show output for subtraction
    def subtract_output (self, diff):
        print (Fore.MAGENTA + "\nANSWER: ", str(diff) + Style.RESET_ALL)

# define multiplication functions
    def multiply_output (self, product):
        print (Fore.MAGENTA + "\nANSWER: ", str(product) + Style.RESET_ALL)

# define division function
    def divide_output (self, quotient):
        print (Fore.MAGENTA + "\nANSWER: "+ str(quotient) + Style.RESET_ALL)

# define additional details
    def ask_user (self):
        username = input(Fore.BLUE + "\nEnter username: " + Style.RESET_ALL)
        print (Fore.GREEN + "\nWelcome to the Calculator, ", username, "!" + Style.RESET_ALL)
        print ()

# define designs:
    def design (self):
        from pyfiglet import Figlet
        font_name = "Block"
        custom_fig = Figlet (font=font_name)
        title = custom_fig.renderText("SIMPLE CALCU")
        print ("-" * 150)
        print (title)
        print ("-" * 150)

# additional operations:
# defining exponent operation function
    def exponent_output (self, exponent):
        print (Fore.MAGENTA + "\nANSWER: "+ str(exponent) + Style.RESET_ALL)
        