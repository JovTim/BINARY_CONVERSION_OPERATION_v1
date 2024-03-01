from decimal_to_binary import decimal_to_binary
from decimal_to_octal import decimal_to_octal
from decimal_to_hexa import decimal_to_hexa

user = '143.5'

def unsign_deci(value):
    print(f"BINARY: {decimal_to_binary(value)}")
    print(f"OCTAL: {decimal_to_octal(value)}")
    print(f"HEXADECIMAL: {decimal_to_hexa(value)}")

#unsign_deci(user)