friends = ["Abhi", "Ananth", "Adarsh", "Amit", "Akhil"]
print (friends)
print(friends[0])   # print value present at given index
print(friends[1:])  # print values from given index till the end of the list
print(friends[len(friends)-2:])
print(friends[1:4]) # print values from index 1 to index 4
print(friends[:3])  # print values from starting of the list to index 3

random_numbers = [1, 3, 5, 4, 7, 8]
dummy_list = []

dummy_list.extend(friends)  # the extend() function appends the list specified in the parenthesis to the calling list
print(dummy_list)
dummy_list.extend(random_numbers)
print(dummy_list)   # lists can contain values of different datatypes
dummy_list.append("ujwal")  # append inserts a single value to the list
print(dummy_list)
dummy_list.insert(2, "ulhas")
print(dummy_list)   # insert() inserts given value (2nd parameter) to given index (1st parameter). All elements from given index are pushed to the right
dummy_list.pop()    # pop() removes the last element
print(dummy_list)
dummy_list.pop(10)  # if index is specified, pop removes that element
print(dummy_list)
print(dummy_list.index("Ananth"))   # gives index of "Ananth"
dummy_list.append("Abhi")
dummy_list.append("Abhi")
print(dummy_list.count("Abhi")) # gives count of the number of occurances of value specified in parenthesis
print(dummy_list.count("Ananya"))   # for values not present, returns 0
random_numbers.sort()   # sorts numbers in ascending order
print(random_numbers)
random_numbers.reverse()
print(random_numbers)

friends2 = friends.copy()   # copies entire list, takes no arguments
print(friends2)

# in operator
if ("Abhi" in friends):
    print("Abhi is a friend")
if ("Aman" not in friends):
    print("Aman is not a friend")
