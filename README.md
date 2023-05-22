# Calculator-OOP

Language: Python

Modules Used:
1. pyfiglet
2. colorama
3. time

Description:
This program is a recreation of the simple_calculator repository I made before.
The difference between the two programs is that this program used the Object
Oriented Programming (OOP) approach, where there are 3 files made:
1. user_interface.py
2. calculator.py
3. main.py

About user_interface.py:

This code represents a calculator program using the OOP (Object-Oriented Programming) concept.
- The code starts with some comments providing the author's name and the purpose of the program.
- The colorama module is imported to enable the usage of colored text in the terminal.
- A class called UserInterface is defined, which serves as the user interface for the calculator.

The UserInterface class has several methods:
1. input_num: Asks the user to enter a number and returns the input as a float.
2. ask_operation: Asks the user to enter an operation (+, -, *, /) and returns the input as a string.
3. add_output, subtract_output, multiply_output, divide_output:
- These methods display the answer of the respective operations (addition, subtraction, multiplication, division)
  along with some stylized formatting.
4. ask_user: Asks the user to enter their username and displays a welcome message.
5. design: Uses the pyfiglet module to create a decorative title for the calculator program.

- The code demonstrates the usage of the colorama module by applying different colors and styles to the printed text.

Overall, this code defines the user interface for a calculator program and provides methods to input numbers,
select operations, display results, and present a visually appealing title.

About calculator.py:

This code defines a class called Calculator, which represents a calculator program using the OOP
(Object-Oriented Programming) concept.

- The code starts with some comments providing the author's name and the purpose of the program.

The Calculator class has several methods:
1. add_input: Takes two input numbers (inp_num1 and inp_num2), adds them together, and returns the sum.
2. subtract_input: Takes two input numbers (inp_num1 and inp_num2), subtracts the second number from the first number, and returns the difference.
3. multiply_input: Takes two input numbers (inp_num1 and inp_num2), multiplies them together, and returns the product.
4. divide_input: Takes two input numbers (inp_num1 and inp_num2), divides the first number by the second number, and returns the quotient.

- Each method performs the respective mathematical operation and returns the result.

Overall, this code defines the functionality of a calculator by providing methods to perform addition, subtraction, multiplication, and division
operations on given input numbers.

About main.py:

This code represents a calculator program using the OOP (Object-Oriented Programming) concept.
- The code begins with some comments providing the author's name and the purpose of the program.
- It imports necessary modules such as colorama for colored output and time for introducing delays in the program.
- It imports the UserInterface class from the user_interface module and the Calculator class from the calculator module.
- An instance of the UserInterface class is created as user_int, and an instance of the Calculator class is created as calcu.
- The code enters a while loop with the condition repeat_prog == "y", which allows the program to repeat as long as the user wants to continue.

Inside the loop:
- The title of the calculator is displayed using the design method of the UserInterface class.
- The user is asked to enter their username using the ask_user method of the UserInterface class.
- The code tries to get input numbers (inp_num1 and inp_num2) from the user using the input_num method of the UserInterface class.
  If a ValueError occurs, an error message is displayed, and the loop continues.
- The user is asked to enter the desired operation using the ask_operation method of the UserInterface class.
- Based on the selected operation, the corresponding method of the Calculator class is called to perform the calculation,
  and the result is displayed using the appropriate output method of the UserInterface class.
- If an invalid operation or a ZeroDivisionError occurs, an error message is displayed, and the loop continues.
- The user is asked if they want to run the program again. If the answer is "n" (no), the program ends; otherwise, the loop continues.
- The code uses the time.sleep function to introduce delays between different parts of the program, giving the user some time to read the output.

Overall, this code creates a calculator program with a user interface, allowing the user to perform calculations by entering input numbers
and selecting the desired operation. The program provides error handling and a loop to repeat the calculation process if the user chooses to continue.
