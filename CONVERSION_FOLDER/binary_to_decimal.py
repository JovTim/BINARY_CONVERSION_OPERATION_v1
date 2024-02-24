from splitter import splitter

user = "1001011.000110011"

def binary_to_decimal(binary):
    numb1, numb2 = splitter(binary)
    whole = 0
    fraction = 0

    if (numb1 and numb2):
        for a in range(1, len(numb1) + 1):
            whole += numb1[-a] * (2 ** (a - 1))
        for b in range(1, len(numb2) + 1):
            fraction += numb2[b-1] * (2 ** (-b))
        return whole + fraction
    else:
        for a in range(1, len(numb1) + 1):
            whole += numb1[-a] * (2 ** (a - 1))
        return whole

print(binary_to_decimal(user))