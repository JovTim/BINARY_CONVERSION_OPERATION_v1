def bin_sign_check(value):
    if value[0] != '1':
        return False
    else:
        return True

def dec_sign_check(value):
    if value[0] != '-':
        return False
    else:
        return True

def oct_sign_check(value):
    if value[0] != '7':
        return False
    else:
        return True

def hex_sign_check(value):
    if value[0] != 'F':
        return False
    else:
        return True