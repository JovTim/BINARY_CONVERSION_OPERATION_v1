user = '011011011100.01100'

def counter(value):
    i = 0

    if '.' in value:
        for i in range(1, len(value) + 1):
            if value[-i] == '.':
                break
            i += 1

        binary = ''
        for j in value:
            if j == '.':
                continue
            binary += j
        return binary, i
    else:
        return value, i

def twoscomplement(value):
    binary, position = counter(value)
    n = len(binary)

    i = n - 1
    while i >= 0:
        if binary[i] == '1':
            break
        i -= 1

    if i == -1:
        return '1' + binary, position
    else:
        k = i - 1
        while k >= 0:
            if binary[k] == '1':
                binary = list(binary)
                binary[k] = '0'
                binary = ''.join(binary)
            else:
                binary = list(binary)
                binary[k] = '1'
                binary = ''.join(binary)
            k -= 1

        return binary, position

def final_phase(value):
    binary, position = twoscomplement(value)

    if position == 0 and '.' not in binary:
        return binary
    else:
        container = list(binary)
        container.insert(-position + 1, '.')

        new_binary = ''.join(container)
        return new_binary

print(final_phase(user))
