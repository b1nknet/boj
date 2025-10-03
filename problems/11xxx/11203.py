line = input().strip()
if line.isdigit():
    print(2**(int(line)+1)-1)
else:
    h, order = line.split()
    node = 2**(int(h)+1)-1
    subtract = 0
    state = ''
    if order[0] == 'L':
        subtract = 1
        state = 'L'
    else:
        subtract = 2
        state = 'R'
    node -= subtract
    for i in range(1, len(order)):
        if state == 'L':
            if order[i] == 'L':
                subtract *= 2
            else:
                subtract = subtract * 2 + 1
                state = 'R'
        else:
            if order[i] == 'L':
                subtract = subtract * 2 - 1
                state = 'L'
            else:
                subtract *= 2
        node -= subtract
    print(node)
