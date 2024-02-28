from binary_to_decimal import binary_to_decimal
from twos_complement import final_phase
from splitter import splitter, hex_replacer

user = "100111.11"

def signed_binary(value):
    #-------------SIGNED DECIMAL---------
    x = final_phase(value)
    decimal = binary_to_decimal(x)

    binary = value

    #return "-" + str(decimal), binary
    print(f"DECIMAL: -{decimal}")
    #-------------SIGNED OCTAL-----------

    oc_binary_whole, oc_binary_frac = splitter(binary)
    oc_whole_container = []
    oc = ""
    for i in range(1, len(oc_binary_whole) + 1):
        if len(oc) == 3:
            oc_whole_container.append(oc)
            oc = ""
        oc = str(oc_binary_whole[-i]) + oc 
    
    if oc:
        for _ in range(3):
            if len(oc) == 3:
                oc_whole_container.append(oc)
                break
            oc = '1' + oc

    octal_whole = ""
    for i in oc_whole_container:
        y = binary_to_decimal(i)
        octal_whole = str(y) + octal_whole

    oc_fraction_container = []
    oc_frac = ""
    for j in oc_binary_frac:
        if len(oc_frac) == 3:
            oc_fraction_container.append(oc_frac)
            oc_frac = ""
        oc_frac += str(j)
    
    if oc_frac:
        for _ in range(3):
            if len(oc_frac) == 3:
                oc_fraction_container.append(oc_frac)
                break
            oc_frac += '0'
    
    octal_fraction = "."
    for j in oc_fraction_container:
        a = binary_to_decimal(j)
        octal_fraction += str(a)

    print(f"OCTAL: {octal_whole + octal_fraction}")
    #-------------SIGNED HEXADECIMAL-----
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
    
    print(f"HEXADECIMAL: {hexa_whole + hexa_fraction}")



signed_binary(user)