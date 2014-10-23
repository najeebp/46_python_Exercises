def test(string):
    if len(string)% 2 == 0:
        mid = len(string) / 2
        start = '[' * mid
        end = ']' * mid
        if string[0:mid] == start and string[mid:] == end:
            return 'OK'
        else:
            return 'NOT OK'
    else:
        return 'NOT OK'
print test('[]][[]')
