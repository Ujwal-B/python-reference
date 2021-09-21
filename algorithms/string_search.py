def rabin_karp(string, pattern):
    str_len = len(string)
    pat_len = len(pattern)
    pat_hash = hash(pattern)
    pos = []
    for i in range(0, str_len - pat_len + 1):
        if hash(string[i:i+pat_len]) == pat_hash:
            pos.append(i)
    return pos

def hash(string, count=0):
    length = len(string)
    for i in range(0, length):
        count += ord(string[i]) * pow(26, length - i - 1) # assumption that we will be using only 26 characters (lowercase letters only)
    return count

pos = rabin_karp(input('Enter a string\n'), input('Enter a pattern\n'))
print(pos)