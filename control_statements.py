a = 10
b = 13

if a > b:
    print ("a is greater than b")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")

# short hand statements

if a < b: print ("a is less than b")

print ("a is greater than b") if a > b else print ("a is not greater than b")

print ("a is greater than b") if a > b else print ("a is equal to b") if a == b else print ("a is less than b")

#conditional operators

if True and True:
    print (True)

if True or False:
    print (True)

if a > b:
    pass    # if there is no statement in the 'if' clause, pass keyword must be used to avoid getting an error
else:
    print ("a is not greater than b")

#continue statement
for i in range(1,10):
    if i == 5:
        continue    # after encountering continue, further statements in the loop is not executed
    print(i)
print("Statement after continue")

#break statement
for char in "Hello":
    if char == "l":
        break       # after encountering break, the loop is terminated, control is passed outside it
    print(char)
print("Statement after break")
