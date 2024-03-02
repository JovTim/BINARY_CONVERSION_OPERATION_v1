def bin_sign_check(value):
    if value[0] != '1':
        return 'Signed binary must start with 1'
    else:
        return value

def dec_sign_check(value):
    if value[0] != '-':
        return 'Signed decimal must start with negative sign'
    else:
        return value

def oct_sign_check(value):
    if value[0] != '7':
        return 'Signed octal must start with 7'
    else:
        return value


def hex_sign_check(value):
    if value[0] != 'F':
        return 'Signed hexadecimal must start with F'
    else:
        return value