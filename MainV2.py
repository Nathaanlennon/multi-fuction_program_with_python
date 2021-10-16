from Class import *
from math import *


def ai():
    print("Hello user, I'm Chara, your personal IA. What's your name?")
    name = input()
    print(f"Hi {name}, I'm happy to meet you ^^")
    print("I have a lot of abilities, try to say someone and if I know how do that, i'll try to help you")
    print("What's your request?")
    request = input()
    if request.casefold() == "addition".casefold() \
            or request.casefold() == "subtraction".casefold() \
            or request.casefold() == "multiplication".casefold() \
            or request.casefold() == "division":
        print(operation(request.lower()))
    if request.casefold() == "complex operation":


def operation(operation_type):
    article = "a"
    if operation_type == "addition":
        article = "an"

    result = 0
    print(
        f"This function has for job to make {article} {operation_type}, "
        f"you write the first number, then the second number. "
        "\nSay \"stop\" to stop the program.")
    i = 1  # i = the number for the while, "number {i}" in the sentence
    while True:
        print(f"What is your number {i}? (stop for stop)")
        number = input()
        if number.casefold() == "stop".casefold():
            break
        try:
            if i == 1:
                result = int(number)
            else:
                if operation_type == "addition":
                    result += int(number)
                elif operation_type == "subtraction":
                    result -= int(number)
                elif operation_type == "multiplication":
                    result *= int(number)
                else:
                    result /= int(number)
        except ValueError:
            print("It's not a number, please retry")
        i += 1
    return f"The result is {result}"





ai()
