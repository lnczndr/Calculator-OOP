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
        print ()
        print ("ANSWER: ", sum)
    
# show output for subtraction
    def subtract_output (self, diff):
        print ()
        print ("ANSWER: ", diff)

# define multiplication functions
    def multiply_output (self, product):
        print ()
        print ("ANSWER: ", product)

# define division function
    def divide_output (self, quotient):
        print ()
        print ("ANSWER: ", quotient)
