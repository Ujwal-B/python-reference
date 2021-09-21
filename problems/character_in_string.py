import sys

def count_characters(string, char):
    count = 0
    for letter in string:
        if char is letter:
            count += 1
    return count

string = str(input("Enter a string: "))
char = str(input("Enter a single character: "))
if len(char) > 1:
    print("You are supposed to enter only one character!")
    sys.exit()
no_of_times = count_characters(string, char)
print("%s occurs %s time(s) in the string \"%s\"" % (char, str(no_of_times), string))
print()