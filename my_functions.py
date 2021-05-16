def introduce_yourself():
    details = []
    name = input("What's your name? : ")
    age = input("How old are you? : ")
    city = input("In which city do you live? : ")

    details.append(name)
    details.append(age)
    details.append(city)
    return details
