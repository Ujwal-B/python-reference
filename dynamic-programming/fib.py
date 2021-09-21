def fib(n, memo = {}):
    if n in memo.keys():
        return memo[n]
    if n < 0:
        return "Error! Negative number given as input"
    if n <= 2:
        return 1
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

res = fib(50)
print(res)