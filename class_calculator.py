#create a class for calculator uses
class Calculator:
    #method Add
    def add(self, number1 , number2):
        sum = number1 + number2
        return sum
    #method Subtract
    def minus(self, number1 , number2):
        difference = number1 - number2
        return difference
    #method Multiply
    def multiply(self, number1 , number2):
        product = number1 * number2
        return product
    #method Divide
    def divide(self, number1, number2):
        quotient = number1 / number2
        return quotient
    #print Sum
    def print_sum(self, sum):
        print("The sum is: " , sum)
    #print Difference
    def print_difference(self, difference):
        print("The difference is: " , difference)
    #print Product
    def print_product(self, product):
        print("The product is: " , product)
    #print Quotient
    def print_quotient(self, quotient):
        print("The quotient is: " , quotient)