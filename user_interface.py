# LANA CAZANDRA U. LEGASPI - BSCPE 1-5
# CALCULATOR USING OOP CONCEPT

# pseudocode
# creating class for "UserInterface" 
class UserInterface:
    
# ask for input
    def input_num (self):
        inp_num = float(input("ENTER NUMBER: "))
        return inp_num
    
# ask for operation
    def ask_operation (self):
        operation = (input("ENTER OPERATION (+, -, *, /): "))
        return operation
    
# show output for addition
    def add_output (self, sum):
        print ("\nANSWER: ", sum)
    
# show output for subtraction
    def subtract_output (self, diff):
        print ("\nANSWER: ", diff)

# define multiplication functions
    def multiply_output (self, product):
        print ("\nANSWER: ", product)

# define division function
    def divide_output (self, quotient):
        print ("\nANSWER: ", quotient)

# define additional details
    def ask_user (self):
        username = input("\nEnter username: ")
        print ("\nWelcome to the Calculator, ", username, "!")
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