from splitter import hexasplitter
def hexa_to_decimal(hexa):
    numb1, numb2 = hexasplitter(hexa)
    whole = 0
    fraction = 0

    if (numb1 and numb2):
        for a in range(1, len(numb1) + 1):
            whole += numb1[-a] * (16 ** (a - 1))

        for b in range(1, len(numb2) + 1):
            fraction += numb2[b-1] * (16 ** (-b))
        
        return whole + fraction
    else:
        for a in range(1, len(numb1) + 1):
            whole += numb1[-a] * (16 ** (a - 1))
        
        return whole


print(hexa_to_decimal('3A4.1B'))


