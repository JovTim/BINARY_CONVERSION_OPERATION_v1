from decimal_to_binary import decimal_to_binary
from twos_complement import final_phase
user = '-20.5'

def signed_deci(value):
    decimal = ""
    for i in value:
        if i == '-':
            continue
        decimal += i

    x = decimal_to_binary(decimal)
    deci = final_phase(x) # signed binary

    #return deci 

    




print(signed_deci(user))

    
    


