from octal_to_decimal import octal_to_decimal
from decimal_to_binary import decimal_to_binary
from octa_to_hexa import final_phase

user = '414.22'

def unsign_octal(value):
    value_2 = str(octal_to_decimal(value))
    print(f"DECIMAL: {value_2}")
    value_3 = decimal_to_binary(value_2)
    print(f"BINARY: {value_3}")
    print(f"HEXADECIMAL: {final_phase(value)}")

#unsign_octal(user)