def say_hi():                                                           # function definition
    name = input ("What's your name? : ")
    print("Hello, " + name[0].upper() + name[1:].lower() + "!")
    agen = input("Enter your age : ")
    age(agen)                                                           # calling another function
    def fav_show():                                                     # inner function
        show_name = input("Which is your favourite show? : ")
        print("Awesome! " + show_name + " is also my favourite show")
    fav_show()                                                          # calling inner function. This function cannot be called outside separately

def age(agenum):
    print("You are " + str(agenum) + " years old!")

# say_hi()                                                                # calling function

def add(num1, num2):
    return num1 + num2

def sqr (num1):
    return num1 * num1

print ("The square of 3 is " + str(sqr(3)))
