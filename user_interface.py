#create a class UserInterface
class UserInterface:
    #constructor of greetings and program description
    def __init__(self , item):
        print("Hello welcome to my programmed " , item)
        print("\033[1;39m `"* 112)
    #method getting the number
    def ask_number(self):
        number = float(input("What is your desired number?: "))
        return number
    #method for asking the what to do in calculator
    def ask_operation(self):
        print("\nChoices:\n1.) add or +\n2.) minus or -\n3.) multiply or *\n4.)divide or /\n")
        operation = input("What is the desired operation?: ")
        return operation