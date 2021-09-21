def canconstruct(targetstr, array, substring = None):
    print(substring)
    if targetstr == '':
        return True
    if len(array) < 1:
        return False
    if substring != None:
        if len(substring) >= len(targetstr) and substring != targetstr:
            return False
    if substring == targetstr:
        return True
    for item in array:
        if substring is None:
            substring = item
        else:
            substring += item
        res = canconstruct(targetstr, array, substring)
        if res is True:
            return True
        if res is False:
            substring = substring[0:len(substring)-len(item)]
    return False

# print(canconstruct('abc', ['a','b','c']))
print(canconstruct('', ['a','b','c']))
print()
print(canconstruct('abcdef', ['bc','ab', 'cd', 'def', 'ef']))
# print(canconstruct('abcdef', ['a', 'aa', 'aaa']))
