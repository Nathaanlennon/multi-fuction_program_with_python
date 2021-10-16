from Class import *


def complex_operation():
    print(
        "The system of the complex operation is easy to understand. You write the operation what you want to resolve. "
        "(Example : 10*(14+2)/25-6)")
    your_operation = input()  # The user write his operation
    first_pile = Pile()  # the first pile to stock the calculation
    calculation_pile = Pile()  # the pile to make parentheses calculations
    open_parentheses = False
    for i in your_operation:
        first_pile.add_element(i)
        if i == "("
def parentheses_verifications:



"""try:

except:
    print("This is not an operation, please retry")"""

complex_operation()
