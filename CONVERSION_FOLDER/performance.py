from twos_complement import final_phase
from binary_to_decimal import binary_to_decimal

#user = '01110.11'

def perform(value):
    if value[0] == '1':
        x = final_phase(value)
        y = binary_to_decimal(x)
        z = '-' + str(y)

        return float(z)
    else:
        return binary_to_decimal(value)

#print(perform(user))