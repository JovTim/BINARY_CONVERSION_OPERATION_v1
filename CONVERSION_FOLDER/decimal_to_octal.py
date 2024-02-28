from splitter import decimalsplitter
user = '39.375'
def decimal_to_octal(decimal):
    whole, fraction = decimalsplitter(decimal)

    # whole number
    samp1 = []
    samp1.append(whole)
    while whole >= 8:
        whole //= 8
        samp1.append(whole)

    remainder = ""
    
    for i in range(1, len(samp1) + 1):
        x = samp1[-i] % 8
        remainder += str(x)

    # fraction

    samp2 = []
    for a in range(24): # range of the decimal point
        num = fraction * 8
        k = str(num)
        l = samp2.append(k[0])
        s = float(k) - int(samp2[a])
        fraction = s
        k = ""

    last = "."

    for b in samp2:
        last += b


    output = int(remainder) + float(last)

    return str(output)

#print(decimal_to_octal(user))

