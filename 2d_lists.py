number_grid = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [0]
]

print(number_grid)
print(number_grid[0])
print(number_grid[2][3])

for row in number_grid:
    print(row)

for row in number_grid:
    for number in row:
        print (number)
