from splitter import decimalsplitter

user = "75.10"

def decimal_to_binary(value):
    whole, fraction = decimalsplitter(value)

    whole_container = []
    whole_container.append(whole)
    while whole >= 2:
        whole //= 2
        whole_container.append(whole)

    remainder = "" # the whole number

    for i in range(1, len(whole_container) + 1):
        x = whole_container[-i] % 2
        remainder += str(x)

    fraction_container = []
    for a in range(24): # range of the decimal point
        num = fraction * 2
        k = str(num)
        l = fraction_container.append(k[0])
        s = float(k) - int(fraction_container[a])
        fraction = s
        k = ""
    
    last = "."

    for b in fraction_container:
        last += b


    output = int(remainder) + float(last)

    return str(output)

print(decimal_to_binary(user))