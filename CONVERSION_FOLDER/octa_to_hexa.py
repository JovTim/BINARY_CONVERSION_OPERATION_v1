from splitter import splitter

user = '77.41'

def octal_to_hexa_phase1(value2):
    user, user2 = splitter(value2)

    whole_container = []
    fraction_container = []

    whole = ""
    fraction = ""

    for i in range(len(user)):
        number = user[i]
        for a in range(3):
            numb = number % 2
            whole += str(numb)
            number //= 2

        fix = ""

        for b in range(1, len(whole) + 1):
            fix += whole[-b]
            
        whole_container.append(fix)
        fix = ""
        whole = ""

    for j in range(len(user2)):
        number2 = user2[j]
        for c in range(3):
            numb2 = number2 % 2
            fraction += str(numb2)
            number2 //=2

        fix2 = ""

        for d in range(1, len(fraction) + 1):
            fix2 += fraction[-d]

        fraction_container.append(fix2)
        fix2 = ""
        fraction = ""

    return whole_container, fraction_container

def octal_to_hexa_phase2(val):
    num1, num2 = octal_to_hexa_phase1(val)

    # -------------whole-------------------

    whole = ""
    for i in num1:
        for j in i:
            whole += j

    lits = [] 
    whole1 = ""
    for i in range(1, len(whole) + 1):
        if len(whole1) == 4:
            lits.append(whole1)
            whole1 = ""
        whole1 = whole[-i] + whole1
    if whole1:
        lits.append(whole1)


    lit = []
    whole_numb = 0
    for i in range(1, len(lits) + 1):
        for j in range(1, len(lits[i - 1]) + 1):
            whole_numb += int(lits[i - 1][-j]) * (2 ** int(j - 1))
        lit.insert(-i, whole_numb)
        whole_numb = 0

    #print(lit)

    # -----------fraction---------

    fraction = ""
    for a in num2:
        for b in a:
            fraction += b

    lits2 = []
    fraction2 = ""
    for a in fraction:
        if len(fraction2) == 4:
            lits2.append(fraction2)
            fraction2 = ""
        fraction2 += a
    if fraction2:
        lits2.append(fraction2)

    if len(lits2[-1]) <= 4:
        for _ in range(4):
            if len(lits2[-1]) == 4:
                break
            lits2[-1] += "0"

    lit2 = []
    fraction_numb = 0
    for a in lits2:
        for b in range(1, len(a) + 1):
            fraction_numb += int(a[-b]) * (2 ** int(b - 1))
        lit2.append(fraction_numb)
        fraction_numb = 0

    #print(lit2)
    return lit, lit2

def final_phase(octal):
    whole_value, fraction_value = octal_to_hexa_phase2(octal)
    hexadecimal = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    whole = ""
    fraction = "."

    for i in whole_value:
        if i in hexadecimal:
            whole += hexadecimal[i]
            continue
        whole += str(i)

    for j in fraction_value:
        if j in hexadecimal:
            fraction += hexadecimal[j]
            continue
        fraction += str(j)

    return whole + fraction

#print(final_phase(user))
#print(octal_to_hexa_phase2(user))

"""
⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠉⢁⣀⣀⣀⡈⠉⠛⢿⡿⠿⢿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠏⢀⣴⣾⣿⣿⣿⣿⣿⡟⠃⢀⣀⣤⣤⣄⠉⢿⣿
⣿⣿⣿⣿⣿⡏⠀⣾⣿⣿⣿⣿⣿⣿⠏⠀⣴⣿⣿⣿⣯⣻⣧⠀⢻
⣿⣿⣿⣿⣿⠁⢸⣿⣿⣿⣿⣿⣿⣿⠀⠸⣿⣿⣿⣿⣿⣿⣿⡇⠈
⣿⣿⣿⣿⡏⠀⣼⣿⣿⣿⣿⣿⣿⣿⣧⠀⠹⢿⣿⣿⣿⡿⠟⠀⣼
⣿⣿⣿⡿⠇⠀⠛⠿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⡈⠉⠀⠀⣴⣿⣿
⣿⡿⠁⣀⢠⢤⣤⠀⠀⠉⢀⠀⠀⠈⠉⠻⢿⣿⣿⣿⡇⠀⣿⣿⣿
⡟⠀⣴⣽⣷⣷⠆⠀⣴⣾⣿⣔⡳⢦⡄⣄⣠⣿⣿⣿⡇⠀⣿⣿⣿
⠀⢰⣿⣿⣿⠇⠀⣼⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⣿⠀⢻⣿⣿
⠀⠸⣾⣿⣿⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿
⣧⠀⠻⢿⣿⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿
⣿⣷⣤⣀⣈⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⠟⠙⣿⣿⣿⡏⠀⣼⣿⣿
⣿⣿⣿⣿⣿⡇⠀⣄⠀⠙⠛⠿⠿⠛⠁⢀⣼⣿⣿⣿⡇⠀⣿⣿⣿
⣿⣿⣿⣿⣿⣷⡀⠘⠿⠶⠀⢀⣤⣤⡀⠙⢿⣿⣿⡿⠁⢰⣿⣿⣿
⢻⣿⣿⣿⣿⣿⣿⣦⣤⣤⣴⣿⣿⣿⣷⣄⣀⠈⠁⣀⣠⣿⣿⣿⣿
⣹⣿⣿⣿⡿⢋⣩⣬⣩⣿⠃⣿⣿⣿⣿⢸⣿⡿⢋⣡⣬⣩⣿⣿⣿
⡗⣿⣿⣿⣧⣈⣛⠛⠻⣿⠀⣿⣿⣿⡿⢸⣿⣧⣈⣛⠛⠻⣿⣿⣿
⣿⣿⣿⣿⠹⣿⣿⡿⠂⣿⣇⠸⣿⣿⠃⣼⣿⠻⣿⣿⡿⠀⣿⣿⣿
⣿⣿⣿⣿⣶⣤⣤⣴⣾⣿⣿⣶⣤⣤⣾⣿⣿⣶⣤⣤⣴⣾⣿⣿⣿
Note: holy finally
"""