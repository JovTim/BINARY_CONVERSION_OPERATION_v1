from splitter import hexasplitter, splitter
from twos_complement import final_phase
from binary_to_decimal import binary_to_decimal

user = '1C.4'
def signed_hex(value):
    user, user2 = hexasplitter(value)
    #-------------SIGNED BINARY----------------
    whole_container = []
    whole = ""

    for i in range(len(user)):
            number = user[i]
            for a in range(4):
                numb = number % 2
                whole += str(numb)
                number //= 2

            fix = ""

            for b in range(1, len(whole) + 1):
                fix += whole[-b]
                
            whole_container.append(fix)
            fix = ""
            whole = ""
            
    fraction_container = []
    fraction = ""
    for j in range(len(user2)):
            number2 = user2[j]
            for c in range(4):
                numb2 = number2 % 2
                fraction += str(numb2)
                number2 //=2

            fix2 = ""

            for d in range(1, len(fraction) + 1):
                fix2 += fraction[-d]

            fraction_container.append(fix2)
            fix2 = ""
            fraction = ""

    final_whole = ""
    for a in whole_container:
            for b in a:
                    final_whole += b
    final_fraction = "."
    for d in fraction_container:
            for f in d:
                    final_fraction += f
    
    binary = final_whole + final_fraction
    print(f"BINARY: {'1111' + binary}")

    #-------------SIGNED DECIMAL--------------
    x = final_phase(binary)
    decimal = binary_to_decimal(x)

    print(f"DECIMAL: -{decimal}")

    #-------------SIGNED OCTAL----------------
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



    
#signed_hex(user)