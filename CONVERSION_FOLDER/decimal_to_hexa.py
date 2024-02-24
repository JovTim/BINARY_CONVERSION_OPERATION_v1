from splitter import decimalsplitter, hex_replacer
user = "15.25"

def decimal_to_hexa(value):
    whole, fraction = decimalsplitter(value)

    whole_container = []
    whole_container.append(whole)
    while whole >= 16:
        whole //= 16
        whole_container.append(whole)
    
    remainder = ""

    if len(whole_container) > 1:
        for i in range(1, len(whole_container), + 1):
            x = whole_container[-i] % 16
            y = hex_replacer(x)
            remainder += str(y)
    else:
        for i in range(len(whole_container)):
            x = whole_container[-i] % 16
            y = hex_replacer(x)
            remainder += str(y)
    
    return remainder

print(decimal_to_hexa(user))