# reading from files

file1 = open("file1.txt", "r")      # opens a file in read mode.
# options to specify in open include r - read, w - write, a - append, r+ - read and write
print(file1.readable())             # checks if the file is in read mode or not
# print(file1.read())                 # reads the entire file
# print(file1.readline())             # reads one line. Reads the line next to the one already read before (if any). else, it reads the first line

# print(file1.readlines()[0])         # puts all lines into a list. Can be accessed through index
# for line in file1.readlines():
    # print(line)

file1.close()

# writing to files

file1 = open("file1.txt", "w")      # w - overwrites the file, a - appends the file
print(file1.writable())
file1.write("This seems to be fine\n")
str1 = "This is another line"
file1.write(str1 + "\n")

file1.close()