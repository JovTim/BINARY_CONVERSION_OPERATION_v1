from hexa_to_decimal import hexa_to_decimal
from decimal_to_octal import decimal_to_octal
from decimal_to_binary import decimal_to_binary
user = '4A.31'

def unsign_hexa(value):
    print(f"DECIMAL: {hexa_to_decimal(value)}")
    value_2 = str(hexa_to_decimal(value))
    value_3 = decimal_to_binary(value_2)
    print(f"BINARY: {value_3}")
    print(f"OCTAL: {decimal_to_octal(value_2)}")

#unsign_hexa(user)