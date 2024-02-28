from splitter import decimalsplitter, hex_replacer, whole_splitter
#user = "123.54"

def decimal_to_hexa(value):
    whole, fraction = decimalsplitter(value)

    whole_container = []
    whole_container.append(whole)
    while whole >= 16:
        whole //= 16
        whole_container.append(whole)
    
    remainder = ""

    for i in range(1, len(whole_container) + 1):
        x = whole_container[-i] % 16
        y = hex_replacer(x)
        remainder += str(y)
    
    fraction_container = []
    for a in range(24): # range of decimal point
        num = fraction * 16
        k = str(num)
        l = fraction_container.append(whole_splitter(k))
        s = float(k) - int(fraction_container[a])
        fraction = s
        k = ""
    
    last = "."

    for b in fraction_container:
        z = hex_replacer(int(b))
        last += str(z)
    
    output = remainder + last

    return str(output)


#print(decimal_to_hexa(user))