def splitter(value):
    binary = []
    number1 = []
    number2 = []

    for i in value:
        binary.append(i)

    for i in range(len(binary)):
        if binary[i] == '.':
            for j in binary[1 + i:]:
                number2.append(int(j))
            break
        number1.append(int(binary[i]))

    return number1, number2
