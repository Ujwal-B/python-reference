def fib(n):
    table = [0 for i in range(0, n+1)]
    # print(table)
    table[1] = 1
    for i in range(0, n):
        table[i+1] += table[i]
        if i+2 <= n:
            table[i+2] += table[i]
    return table[n]

print(fib(5))
print(fib(50))
# print(fib(500))
# print(fib(5000))
# print(fib(50000))