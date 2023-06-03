from class_calculator import Calculator
from user_interface import UserInterface

class DanielCalculator(Calculator , UserInterface):
    def add_new(self, number1 , number2):
        try:
            sum = number1 + number2
            return sum
        except ValueError:
            print("Your input must be a integer")
    
    def minus_new(self, number1 , number2):
        try:
            difference = number1 - number2
            return difference
        except ValueError:
            print("Your input must be a integer")
    
    def multiply_new(self, number1 , number2):
        try:
            product = number1 * number2
            return product
        except ValueError:
            print("Your input must be a integer")
    
    def divide_new(self, number1, number2):
        try:
            quotient = number1 / number2
            return quotient
        except ValueError:
            print("Your input must be a integer")
        except ZeroDivisionError:
            print("You are dividing by Zero")