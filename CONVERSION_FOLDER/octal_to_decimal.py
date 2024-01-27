from splitter import splitter

user = '611.7'
# Since first draft palang ito, wag mo muna lagyan ng conditional 
# statement (number >= 8)
def octal_to_decimal(octal):
    numb1, numb2 = splitter(octal)
    whole = 0
    fraction = 0

    if (numb1 and numb2):
        for a in range(1, len(numb1) + 1):
            whole += numb1[-a] * (8 ** (a - 1))
        for b in range(1, len(numb2) + 1):
            fraction += numb2[b-1] * (8 ** (-b))

        return whole + fraction
    else:
        for a in range(1, len(numb1) + 1):
            whole += numb1[-a] * (8 ** (a - 1))
        return whole 

print(octal_to_decimal(user))