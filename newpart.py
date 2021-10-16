import random


def encrypt2():
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
    print(encrypt_1)
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


encrypt2()


# test text : c.hbii$hb#fegkwdat
# [106, 39, 97, 105, 109, 101, 32, 108, 101, 32, 99, 104, 111, 99, 111, 108, 97, 116]
# test key : 5GhRC74380

def decrypt2():
    text_2 = []
    key_2 = []
    key_3 = []
    decrypt_1 = []
    decrypt_2 = ""
    num = []
    print("Welcome in the decrypter tools. You have to give encrypt text and encrypt key for decrypt your text.")
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


decrypt2()
