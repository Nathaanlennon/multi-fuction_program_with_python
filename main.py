from random import *
import random

name = "random_name"
stop = "stop"
x = "none"


def ia():
    global name
    global stop
    global x
    print("hey user, what's your name ?")
    name = input()
    print(f"hi {name}, I'm Chara, your personal IA. If you want something, you just have to ask")
    print("What is your question ?")
    while x != "stop":
        x = input("")
        if "take" and "addition" in x:
            addition()

        if "how are you" in x:
            print("I'm fine, thank you")
            input("and you ?")

        if "substraction" in x:
            substraction()

        if "multiplication" in x:
            multiplication()

        if "division" in x:
            division()

        if "operation" in x:
            operation()

        if "encrypt" in x or "decrypt" in x or "codex" in x:
            codex()


def addition():
    i = 1
    r = 1
    result = 0
    add = 0
    while r == 1:
        add = input(f"What's your number {i} ? (stop for stop)")
        if add == "stop":
            r = 0
        else:
            add = int(add)
            result += add
        i += 1
    print(result)


def substraction():
    i = 1
    r = 1
    result = 0
    sub = 0
    while r == 1:
        sub = input(f"What's your number {i} ? (stop for stop)")
        if sub == "stop":
            r = 0
        else:
            sub = int(sub)
            if i == 1:
                result = sub
            else:
                result -= sub
        i += 1
    print(result)


def multiplication():
    i = 1
    r = 1
    result = 0
    while r == 1:
        mult = input(f"What's your number {i} ? (stop for stop)")
        if mult == "stop":
            r = 0
        else:
            mult = int(mult)
            if i == 1:
                result = mult
            else:
                result *= mult
        i += 1
    print(result)


def division():
    global x
    i = 1
    r = 1
    result = 0
    if "euclidean division" in x:
        other = 0
        while i != 3:
            div = input(f"What's your number {i} ? (stop for stop)")
            if div == "stop":
                r = 0
            else:
                div = int(div)
                if i == 1:
                    result = div
                else:
                    other = (result % div)
                    result //= div
            i += 1
        print(result, other)
    else:
        while r == 1:
            div = input(f"What's your number {i} ? (stop for stop)")
            if div == "stop":
                r = 0
            else:
                div = int(div)
                if i == 1:
                    result = div
                else:
                    result /= div
            i += 1
    print(result)


def operation():
    num = 1
    ope = []
    r = 1
    x = input(f"What's your number {num}?")
    if x == "stop":
        return
    else:
        ope += [x]
    while r != 0:
        sign = input("What's your operation ? (stop for stop)")
        if sign == "stop":
            r = 0
        elif sign == "plus" or sign == "+":
            ope += ["+"]
        elif sign == "minus" or sign == "-":
            ope += ["-"]
        elif sign == "times" or sign == "*":
            ope += ["*"]
        elif sign == "over" or sign == "/":
            ope += ["/"]
        num += 1
        if r != 0:
            ope += [input(f"What's your number {num} ?")]
    print(ope)
    a = input("it's your calculation ?")
    if a == "yes":
        res = False
        while not res:
            index = 0
            sign = "none"
            if "*" in ope or "/" in ope:
                while "*" in ope or "/" in ope:
                    sign = (ope[index])
                    index += 1
                    if sign == "*":
                        x = float(ope[(ope.index("*") - 1)])
                        y = float(ope[(ope.index("*") + 1)])
                        re = x * y
                        ope.pop(ope.index("*") - 1)
                        ope.pop(ope.index("*") + 1)
                        ope.insert((ope.index("*") + 1), re)
                        ope.pop(ope.index("*"))
                        index = 0

                    elif sign == "/":
                        x = float(ope[(ope.index("/") - 1)])
                        y = float(ope[(ope.index("/") + 1)])
                        re = x / y
                        ope.pop(ope.index("/") - 1)
                        ope.pop(ope.index("/") + 1)
                        ope.insert((ope.index("/") + 1), re)
                        ope.pop(ope.index("/"))
                        index = 0

            else:
                while "+" in ope or "-" in ope:
                    sign = (ope[index])
                    index += 1

                    if sign == "+":
                        x = float(ope[(ope.index("+") - 1)])
                        y = float(ope[(ope.index("+") + 1)])
                        re = x + y
                        ope.pop(ope.index("+") - 1)
                        ope.pop(ope.index("+") + 1)
                        ope.insert((ope.index("+") + 1), re)
                        ope.pop(ope.index("+"))
                        index = 0

                    elif sign == "-":
                        x = float(ope[(ope.index("-") - 1)])
                        y = float(ope[(ope.index("-") + 1)])
                        re = x - y
                        ope.pop(ope.index("-") - 1)
                        ope.pop(ope.index("-") + 1)
                        ope.insert((ope.index("-") + 1), re)
                        ope.pop(ope.index("-"))
                        index = 0

                else:
                    res = True

        print(ope)
    elif a == "no":
        operation()


def codex():
    print("It's \"The Codex\", a special encryptor. You can encrypt and decrypt texts.")
    choice1 = "[1]"
    choice2 = "[2]"
    print(f"{choice1} encrypt")
    print(f"{choice2} decrypt")
    choice = input("")
    if choice == "1" or choice == "[1]":
        print("choose encrypt level (1, 2, 3)")
        choice2 = input("")
        if choice2 == "1":
            code = []
            encrypt_1 = []
            encrypt_2 = ""
            print("What's your text ?")
            text = input("")
            for i in range(len(text)):
                a = text[i]
                code.append(a)
            print(code)
            for i in range(len(code)):
                a = ord(code[i])
                encrypt_1.append(a)
            print(encrypt_1)
            for i in range(len(encrypt_1)):
                a = chr((encrypt_1[i] + 1))
                encrypt_2 += a
            print(encrypt_2)
        if choice2 == "2":
            code = []
            code2 = ""
            encrypt_1 = []
            encrypt_2 = ""
            num_loop = 0
            print("What's your text ?")
            text = input("")
            for i in range(len(text) // 4):
                random.randint(0, 1)
                if random == 0:
                    code.append(str(chr(random.randint(33, 47))))
                else:
                    code.append(str(chr(random.randint(58, 127))))
                code2 += code[i]
            for i in range(len(text)):
                encrypt_1.append(ord(text[i]))
            while encrypt_1:
                num = random.randint(0, 10)
                code2 += str(num)
                for i in range(len(code)):
                    if encrypt_1:
                        if (ord(code[i]) % 2) == 0:
                            if (encrypt_1[0] + num) > 127:
                                encrypt_2 += (chr(encrypt_1[0]))
                                encrypt_2 += "123"
                            else:
                                encrypt_2 += (chr(encrypt_1[0] + num))
                        if (ord(code[i]) % 2) == 1:
                            if (encrypt_1[0] - num) < 32:
                                encrypt_2 += (chr(encrypt_1[0]))
                                encrypt_2 += "123"
                            else:
                                encrypt_2 += (chr(encrypt_1[0] - num))
                        encrypt_1.pop(0)
                num_loop += 1
            code3 = str(num_loop)
            for i in range(len(code2)):
                code3 += code2[i]
            print("Your encrypt text is :", encrypt_2)
            print("And the key is :", code3)
    if choice == "2" or choice == "[2]":
        print("choose decrypt level (1, 2, 3)")
        choice2 = input("")
        if choice2 == "1":
            code = []
            decrypt_1 = []
            decrypt_2 = ""
            print("What's your encrypt text ?")
            text = input("")
            for i in range(len(text)):
                a = text[i]
                code.append(a)
            print(code)
            for i in range(len(code)):
                a = ord(code[i])
                decrypt_1.append(a)
            print(decrypt_1)
            for i in range(len(decrypt_1)):
                a = chr((decrypt_1[i] - 1))
                decrypt_2 += a
            print(decrypt_2)
        if choice2 == "2":
            text_2 = []
            key_2 = []
            key_3 = []
            decrypt_1 = []
            decrypt_2 = ""
            num = []
            print(
                "Welcome in the decrypter tools. You have to give encrypt text and encrypt key for decrypt your text.")
            print("text :")
            text = input("")
            print("key :")
            key = input("")
            sizetext = int(key[0])
            for i in range(len(key)):
                key_2.append(key[i])
            key_2.pop(0)
            for i in range(len(key_2)):
                if key_2:
                    if not key_2[0].isdigit():
                        key_3.append(key_2[0])
                    else:
                        num.append(int(key_2[0]))
                    key_2.pop(0)
            for i in range(len(text)):
                text_2.append(text[i])
            for i in range(len(text_2)):
                if text_2[i + 3:]:
                    if text_2[i + 1] == "1":
                        if text_2[i + 2] == "2":
                            if text[i + 3] == "3":
                                decrypt_1.append(text[i] + text[i + 1] + text[i + 2] + text[i + 3])
                                for i in range(3):
                                    text_2.pop(i + 1)
                    else:
                        decrypt_1.append(text[i])
                else:
                    decrypt_1.append(text[i])
            while decrypt_1:
                if num:
                    for i in range(len(key_3)):
                        if decrypt_1:
                            if (ord(key_3[i]) % 2) == 0:
                                if "123" in (decrypt_1[0]):
                                    a = (decrypt_1[0])
                                    a = a[0]
                                    decrypt_2 += a
                                    decrypt_1.pop(0)
                                else:
                                    decrypt_2 += (chr(ord(decrypt_1[0]) - num[0]))
                                    decrypt_1.pop(0)
                            elif (ord(key_3[i]) % 2) == 1:
                                if "123" in decrypt_1[0]:
                                    a = decrypt_1[0]
                                    a = a[0]
                                    decrypt_2 += a
                                    decrypt_1.pop(0)
                                else:
                                    decrypt_2 += (chr(ord(decrypt_1[0]) + num[0]))
                                    decrypt_1.pop(0)
                    num.pop(0)
            print(f"the decrypt text is \"{decrypt_2}\"")


ia()
