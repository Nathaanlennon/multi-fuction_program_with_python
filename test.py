"""import random

code = []
code2 = ""
encrypt_1 = []
encrypt_2 = ""
num_loop = 0
print("What's your text ?")
text = "j'aime le chocolat"#input("")
for a in range(len(text) // 4):
    random.randint(0, 1)
    if random == 0:
        code.append(str(chr(random.randint(33, 47))))
    else:
        code.append(str(chr(random.randint(58, 127))))
    code2 += code[a]
for b in range(len(text)):
    encrypt_1.append(ord(text[b]))
print(encrypt_1)
while encrypt_1:
    num = random.randint(0, 10)
    code2 += str(num)
    for c in range(len(code)):
        if encrypt_1:
            if (ord(code[c]) % 2) == 0:
                if (encrypt_1[0] + num) > 127:
                    encrypt_2 += (chr(encrypt_1[0]))
                    encrypt_2 += "123"
                else:
                    encrypt_2 += (chr(encrypt_1[0] + num))
            if (ord(code[c]) % 2) == 1:
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

# test text : c.hbii$hb#fegkwdat
# [106, 39, 97, 105, 109, 101, 32, 108, 101, 32, 99, 104, 111, 99, 111, 108, 97, 116]
# test key : 5GhRC74380

text_2 = []
key_2 = []
key_3 = []
decrypt_1 = []
decrypt_2 = ""
num = []
print("Welcome in the decrypter tools. You have to give encrypt text and encrypt key for decrypt your text.")
print("text :")
text = encrypt_2 #input("")
print("key :")
key = code3 #input("")
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
for j in range(len(text)):
    text_2.append(text[j])
for k in range(len(text_2)):
    if text_2[k + 3:]:
        if text_2[k + 1] == "1":
            if text_2[k + 2] == "2":
                if text[k + 3] == "3":
                    decrypt_1.append(text[k] + text[k + 1] + text[k + 2] + text[k + 3])
                    for l in range(3):
                        text_2.pop(k + 1)
        else:
            decrypt_1.append(text[k])
    else:
        decrypt_1.append(text[k])
while decrypt_1:
    if num:
        for m in range(len(key_3)):
            if decrypt_1:
                if (ord(key_3[m]) % 2) == 0:
                    if "123" in (decrypt_1[0]):
                        a = (decrypt_1[0])
                        a = a[0]
                        decrypt_2 += a
                        decrypt_1.pop(0)
                    else:
                        decrypt_2 += (chr(ord(decrypt_1[0]) - num[0]))
                        decrypt_1.pop(0)
                elif (ord(key_3[m]) % 2) == 1:
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
"""
"""
import random

code = []
code2 = ""
encrypt_1 = []
encrypt_2 = ""
num_loop = 0
print("What's your text ?")
text = "j'aime le chocolat"#input("")
for a in range(len(text) // 4):
    random.randint(0, 1)
    if random == 0:
        code.append(str(chr(random.randint(33, 47))))
    else:
        code.append(str(chr(random.randint(58, 127))))
    code2 += code[a]
for b in range(len(text)):
    encrypt_1.append(ord(text[b]))
print(encrypt_1)
chuech = []
for i in range(len(encrypt_1)):
    chuech.append(encrypt_1[i])
for x in range(10):
    encrypt_2 = ""
    encrypt_1 = []
    for i in range(len(chuech)):
        encrypt_1.append(chuech[i])
    while encrypt_1:
        num = x
        code2 += str(num)
        for c in range(len(code)):
            if encrypt_1:
                if (ord(code[c]) % 2) == 0:
                    if (encrypt_1[0] + num) > 127:
                        encrypt_2 += (chr(encrypt_1[0]))
                        encrypt_2 += "123"
                    else:
                        encrypt_2 += (chr(encrypt_1[0] + num))
                elif (ord(code[c]) % 2) == 1:
                    if (encrypt_1[0] - num) < 32:
                        encrypt_2 += (chr(encrypt_1[0]))
                        encrypt_2 += "123"
                    else:
                        encrypt_2 += (chr(encrypt_1[0] - num))
                encrypt_1.pop(0)
    print(encrypt_2)

print("ok")


decrypt_1"""
tab=[]

def cell_menu():
    for i in range(len(tab)):
        
        cell_menu()
if "?" in tab[d]:
    print("Choose line and column (ex : \"1:0\")")
    print("For place or remove a flag, just say \"flag\")")
    choice = input("")
    choice_bomb = []
    if choice == "flag":
        print("Choose line and column (ex : \"1:0\")")
        flag = input("")
        choice_flag = []
        for i in range(len(flag)):
            choice_flag.append(flag[i])
        flag_line = int(choice_flag[0])
        flag_column = int(choice_flag[-1])
        if tab[flag_line][flag_column] == "?":
            tab[flag_line].pop(flag_column)
            tab[flag_line].insert(flag_column, "F")
            print("\n".join([repr(x) for x in tab]))
        elif tab[flag_line][flag_column] == "F":
            tab[flag_line].pop(flag_column)
            tab[flag_line].insert(flag_column, "?")
            print("\n".join([repr(x) for x in tab]))
        else:
            print("Hum...it's just impossible")
    else:
        for i in range(len(choice)):
            choice_bomb.append(choice[i])
        for j in range(len(index_bomb)):
            for k in range(len(choice)):
                if choice[k] != ":":
                    if c == 1:
                        a = int(choice[k])
                    elif c == 2:
                        b = int(choice[k])
                    c += 1
            if tab[a][b] == "F":
                print("just impossible sorry")
            else:
                if choice == index_bomb[j]:
                    tab[a].pop(b)
                    tab[a].insert(b, "B")
                    print("\n".join([repr(x) for x in tab]))
                    print("you have lost")
                    exit()
                else:
                    bomb_around = 0
                    for i in range(len(tab)):
                        for j in range(len(tab[i])):
                            if (i == int(choice_bomb[0]) or i == (int(choice_bomb[0]) - 1) or i == (
                                    int(choice_bomb[0]) + 1)) and (
                                    j == int(choice_bomb[-1]) or j == (int(choice_bomb[-1]) - 1) or j == (
                                    int(choice_bomb[-1]) + 1)):
                                index_test = f"{i}:{j}"
                                if (index_test != choice) and (index_test in index_bomb):
                                    bomb_around += 1
                    tab[a].pop(b)
                    tab[a].insert(b, str(bomb_around))
                    print("\n".join([repr(x) for x in tab]))