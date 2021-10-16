class Operation:
    def __init__(self, first, sign, second):
        # "first" == the first number, second == the second number and "sign" == the calculation sign (-+*/)
        self.__number_one = first
        self.__number_two = second
        self.__calculation_sign = sign

    def __str__(self):
        if self.__calculation_sign == "+":
            return self.__number_one + self.__number_two
        elif self.__calculation_sign == "-":
            return self.__number_one - self.__number_two
        elif self.__calculation_sign == "*":
            return self.__number_one * self.__number_two
        elif self.__calculation_sign == "/":
            return self.__number_one / self.__number_two


class Pile:
    def __init__(self):
        self.__pile = []

    def add_element(self, element):
        self.__pile.append(element)

    def delete_element(self):
        self.__pile.pop()
    def print_pile(self):
        return self.__pile
    def __str__(self):
        return self.__pile
