from class_calculator import Calculator
from user_interface import UserInterface

class DanielCalculator(Calculator , UserInterface):
    def add(self, number1 , number2):
        sum = number1 + number2
        return sum