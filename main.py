name = "random_name"
stop = "stop"
x = "none"


def ia():
    global name
    global stop
    global x
    name = input("hey user, what's your name ?")
    print(f"hi {name}, I'm Chara, your personal IA. If you want something, you just have to ask")
    print("What is your question ?")
    while x != "stop":
        x = input("")
        if "take" and "addition" in x:
            addition()

        '''if "how are you" in x:
            print("I'm fine, tank you")
            input("and you ?")'''

        if "substraction" in x:
            substraction()

        if "multiplication" in x:
            multiplication()

        if "division" in x:
            division()


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
    mult = 0
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
    div = 0
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


ia()
