from performance import perform
from decimal_to_binary import decimal_to_binary
from twos_complement import final_phase

user1 = '11101.110'
user2 = '1010.101'

def bin_multiplication(value1, value2):
    numb1 = perform(value1)
    numb2 = perform(value2)

    calculate = str(numb1 * numb2)

    decimal = ''

    if calculate[0] == '-':
        for i in calculate:
            if i == '-':
                continue
            decimal += i
        
        x = decimal_to_binary(decimal)
        deci = final_phase(x)
        return '(1111)' + str(deci)
    else:
        return decimal_to_binary(calculate)

#print(bin_multiplication(user1, user2))
