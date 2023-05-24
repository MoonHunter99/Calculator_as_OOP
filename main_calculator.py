#call all the class that is needed
from class_calculator import Calculator
from user_interface import UserInterface
#create a instance object for the classes
ui = UserInterface("Calculator")
calc = Calculator()
#get the first numbers
first_number = ui.ask_number()
#get the second number
second_number = ui.ask_number()
#ask the user what method to use
operation = ui.ask_operation()
#check using if else on what method in calculator to use
#print the result
if operation == "+" or "add":
    sum = calc.add(first_number , second_number)
    calc.print_sum(sum)
elif operation == "-" or "minus":
    difference = calc.minus(first_number , second_number)
    calc.print_difference(difference)
elif operation == "*" or "multiply":
    product = calc.multiply(first_number, second_number)
    calc.print_product(product)
elif operation == "/" or "divide":
    quotient = calc.divide(first_number , second_number)
    calc.print_quotient(quotient)