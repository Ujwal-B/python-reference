# Given a string and a number k, shift the characters of the string k positions to the right
# If the new string forms a few same words as the old one, return the number of correct words formed

def changed_order(string, k):
    words = string.split()
    print(words)
    new_string = []
    for word in words:
        new_word = []
        i = 0
        wordlen = len(word)
        while i != wordlen:
            new_word.append(word[(i + k) % wordlen])
            i += 1
        temp = ''.join(new_word)
        new_string.append(temp)
    print(new_string)
    # count the number of words which appear the same
    count = i = 0
    for word in new_string:
        if word == words[i]:
            count += 1
        i += 1
    return count

ostring = "hello there how are you"
k = 30
no_of_same_words = changed_order(ostring, k)
# nstring = ''.join(nstring)
print(no_of_same_words)