#call all the class that is needed
from daniel_calculator import DanielCalculator
#create a instance object for the classes
daniel = DanielCalculator("Calculator")
#get the first numbers
#get the second number
#ask the user what method to use
operation = daniel.ask_operation()
#check using if else on what method in calculator to use
#print the result
if operation == "add":
    first_number = daniel.ask_number()
    second_number = daniel.ask_number()
    sum = daniel.add_new(first_number , second_number)
    daniel.print_sum(sum)
elif operation =="minus":
    first_number = daniel.ask_number()
    second_number = daniel.ask_number()
    difference = daniel.minus_new(first_number , second_number)
    daniel.print_difference(difference)
elif operation == "multiply":
    first_number = daniel.ask_number()
    second_number = daniel.ask_number()
    product = daniel.multiply_new(first_number, second_number)
    daniel.print_product(product)
elif operation == "divide":
    first_number = daniel.ask_number()
    second_number = daniel.ask_number()
    quotient = daniel.divide_new(first_number , second_number)
    daniel.print_quotient(quotient)