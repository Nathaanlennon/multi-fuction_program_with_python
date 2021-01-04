import random

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
            print("What's your text ?")
            text = input("")
            for i in range(len(text) // 4):
                code.append(str(chr(random.randint(33, 127))))
                code2 += code[i]
            for i in range(len(text)):
                encrypt_1.append(ord(text[i]))
            print(encrypt_1)
            while encrypt_1:
                num = random.randint(0, 10)
                code2 += str(num)
                for i in range(len(code)):
                    if encrypt_1:
                        if (ord(code[i]) % 2) == 0:
                            if (encrypt_1[0] + num) > 127:
                                encrypt_2 += (chr(encrypt_1[0]))
                                encrypt_2 += "1"
                            else:
                                encrypt_2 += (chr(encrypt_1[0] + num))
                        if (ord(code[i]) % 2) == 1:
                            if (encrypt_1[0] - num) < 32:
                                encrypt_2 += (chr(encrypt_1[0]))
                                encrypt_2 += "1"
                            else:
                                encrypt_2 += (chr(encrypt_1[0] - num))
                        encrypt_1.pop(0)

            print("Your encrypt text is :", encrypt_2)
            print("And the key is :", code2)
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
        #if choice2 == "2":



codex()
