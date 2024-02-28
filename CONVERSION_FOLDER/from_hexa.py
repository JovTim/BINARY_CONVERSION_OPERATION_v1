from splitter import hexasplitter
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
    binary = '1111' + binary
    print(f"BINARY: {binary}")

    #-------------SIGNED DECIMAL--------------
    x = final_phase(binary)
    decimal = binary_to_decimal(x)

    print(f"DECIMAL: -{decimal}")

    #-------------SIGNED OCTAL----------------

    

print(signed_hex(user))