# while
i = 1
while i <= 5:
    print(str(i) + " is the current iteration number")
    i += 1

# for
for letter in "Control Statements":
    print(letter.upper())

friends = ["Abhi", "Adarsh", "Amulya", "Aakash"]
for friends_name in friends:
    print(friends_name)

for index in range(10):     # takes numbers from 0 to 9
    print(index*index)
print()

for index in range(4,10):   #includes first number in range, not the second number, so basically from 4 to 9
    print(index*index*index)
print()

for index in range(len(friends)):
    print(index)            #prints the indexes of friends list
print()
