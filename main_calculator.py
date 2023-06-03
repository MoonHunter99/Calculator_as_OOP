#call all the class that is needed
from daniel_calculator import DanielCalculator
#create a instance object for the classes
daniel = DanielCalculator("Cassio")
#get the first numbers
first_number = daniel.ask_number()
#get the second number
second_number = daniel.ask_number()
#ask the user what method to use
operation = daniel.ask_operation()
#check using if else on what method in calculator to use
#print the result
if operation == "+" or "add":
    sum = daniel.add(first_number , second_number)
    daniel.print_sum(sum)
elif operation == "-" or "minus":
    difference = daniel.minus(first_number , second_number)
    daniel.print_difference(difference)
elif operation == "*" or "multiply":
    product = daniel.multiply(first_number, second_number)
    daniel.print_product(product)
elif operation == "/" or "divide":
    quotient = daniel.divide(first_number , second_number)
    daniel.print_quotient(quotient)