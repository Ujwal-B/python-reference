# exception handling

try:
	print(Something)

except:		# catches error arising from the above try block
	print("Don't be a donut!")


try:
	a = int(input("Enter a number: "))
	print(a)

except ValueError:
	print("Wrong type of value error caught")

try:
	10/0

except ZeroDivisionError:
	print("Zero division error caught!")

try:
	numbers = [1, 2, 3, 4, 5]
	print(numbers[6])

except IndexError as err:
	print (err)

