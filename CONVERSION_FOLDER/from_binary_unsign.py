from binary_to_decimal import binary_to_decimal
from decimal_to_octal import decimal_to_octal
from octa_to_hexa import final_phase


#user = '100111.011'
def unsign_binary(value):
    print(f"DECIMAL: {binary_to_decimal(value)}")
    value_2 = str(binary_to_decimal(value))
    print(f"OCTAL: {decimal_to_octal(value_2)}")
    value_3 = str(final_phase(value_2))
    print(f"HEXADECIMAL: {value_3}")
    


#unsign_binary(user)