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
