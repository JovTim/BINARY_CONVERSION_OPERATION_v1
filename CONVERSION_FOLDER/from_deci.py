from decimal_to_binary import decimal_to_binary
from twos_complement import final_phase
from splitter import splitter, hex_replacer
from binary_to_decimal import binary_to_decimal

user = '-33.125'

def signed_deci(value):
    decimal = ""
    for i in value:
        if i == '-':
            continue
        decimal += i

    x = decimal_to_binary(decimal)
    deci = '1111' + final_phase(x) # signed binary
    # try pa mag add ng 1111 sa dulo
    print(f"Binary: {deci}")
    #return x, deci

    #---------------------SIGNED OCTAL---------------
    oc_binary_whole, oc_binary_frac = splitter(deci)
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
    
    octal_whole =""

    for i in oc_whole_container:
        y = binary_to_decimal(i)
        octal_whole = str(y) + octal_whole
    
    #return octal_whole
        
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

    
    #return octal_whole + octal_fraction
    print(f"OCTAL: {octal_whole + octal_fraction}")
    
    #----------------------SIGNED HEXADECIMAL----------------
    he_binary_whole, he_binary_frac = splitter(deci)
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
    
    #return hexa_whole
        
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
    

    #return oc_binary_whole, oc_binary_frac, he_binary_whole, he_binary_frac



#signed_deci(user)

    
    


