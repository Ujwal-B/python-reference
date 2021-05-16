print("This")
print("is a\nString")   # '\n' is next line
print("This is \"quotation mark\" being printed") # '\' is escape character

institution_name = "YOLO"

print(institution_name)
print(institution_name + " is a weird name")

print(institution_name.lower()) # converts entire string into lower characters
print(institution_name.upper()) # converts entire string into lower characters
print(institution_name.islower())   # checks whether all characters in the string is uppercase
print(institution_name.lower().islower()) # converts all characters into lower first, then checks if all characters are lower
print(len(institution_name))    # prints length of string
print(institution_name[0])  # prints the 1st character (0th index)
print(institution_name.index("L")) # prints the index of the character. If multiple characters are there, prints the index of 1st char
print(institution_name.index("LO")) # prints the starting index of the substring
print(institution_name.replace("YO", "SO")) # replaces given substring, no change if incorrect substring is given

# string comparision
if "dog" == "dog":              # unicodes of each character is compared
    print("Equals")
if "dog" < "cat":
    print("Less than")
elif "dog" > "cat":
    print("Greater than")

str1 = "This is a dog"
str2 = "This is not a dog"
str3 = "This is a cat"

if (str1 is str1): print ("Statements 1 and 2 are same")    # is operator checks if both operators are referring to the same object
print ("Statements 2 and 3 are same") if (str2 is str3) else print ("Statements 1 and 2 are same") if (str1 is str2) else print ("These statements aren't same")
if (str1 is not str2):
    print("The 2 statements are not the same")      # is not works like is but checks if they are not referring to the same object
