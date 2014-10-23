target = 'tiger'
input = raw_input('enter words')
while input != target:
    output = ' '
    for pos in range(len(input)):
        if input[pos] in target:
            if target[pos] == input[pos]:
                output += '[' + input[pos] + ']'
            else:
                output += '(' + input[pos] + ')'
        else:
            output += input[pos]

    print "clue: " + output
    input = raw_input('enter words')

print "Found"