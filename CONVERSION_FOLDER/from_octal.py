from splitter import splitter, hex_replacer
from octa_to_hexa import octal_to_hexa_phase1
from twos_complement import final_phase
from binary_to_decimal import binary_to_decimal
user = "36.51"

def signed_octal(value):
    #------------SIGNED BINARY--------------
    whole, fraction = octal_to_hexa_phase1(value)

    whole_container = ""
    for i in whole:
        for j in i:
            whole_container += j

    fraction_container = "."
    for a in fraction:
        for b in a:
            fraction_container += b

    binary = whole_container + fraction_container

    print(f"BINARY: {binary}")

    #------------SIGNED DECIMAL-------------
    x = final_phase(binary)
    decimal = binary_to_decimal(x)

    print(f"DECIMAL: -{decimal}")
    #------------SIGNED HEXADECIMAL---------
    he_binary_whole, he_binary_frac = splitter(binary)
    he_whole_container = []
    hexa = ""
    for i in range(1, len(he_binary_whole) + 1):
        if len(hexa) == 4:
            he_whole_container.append(hexa)
            hexa = ""
        hexa = str(he_binary_whole[-i]) + hexa
    
    if hexa:
        for _ in range(4):
            if len(hexa) == 4:
                he_whole_container.append(hexa)
                break
            hexa = '1' + hexa

    hexa_whole = ""
    for i in he_whole_container:
        y = binary_to_decimal(i)
        convert = hex_replacer(int(y))
        hexa_whole = str(convert) + hexa_whole
    
    hex_fraction_container = []
    hex_frac = ""
    for j in he_binary_frac:
        if len(hex_frac) == 4:
            hex_fraction_container.append(hex_frac)
            hex_frac = ""
        hex_frac += str(j)

    if hex_frac:
        for _ in range(4):
            if len(hex_frac) == 4:
                hex_fraction_container.append(hex_frac)
                break
            hex_frac += '0'
    
    hexa_fraction = "."
    for j in hex_fraction_container:
        a = binary_to_decimal(j)
        convert1 = hex_replacer(a)
        hexa_fraction += str(convert1)
    
    print(f"HEXADECIMAL: {hexa_whole + hexa_fraction }")


#signed_octal(user)