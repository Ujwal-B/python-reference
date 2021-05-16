month_conversions = {           # dictionaries are written in this format
    # define key : value pairs, separated by commas
    # keys are to be unique
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
}

print(month_conversions["Jan"])
print(month_conversions.get("Mar"))
print(month_conversions.get("Abc", "Not a valid key"))  # if given key does not match any key in the dictionary, the 2nd parameter is printed
print(month_conversions.get("Apr", "Not a valid key"))  # since a valid key is passed, the error message is not printed.
