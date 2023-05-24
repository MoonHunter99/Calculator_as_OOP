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
#check using if else on what method in calculator to use
#print the result