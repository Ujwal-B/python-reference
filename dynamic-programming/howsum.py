p = []
def howsum(targetsum, array, memo={}):
    print(targetsum)
    if targetsum in memo.keys():
        return memo[targetsum]
    if targetsum < 0:
        return None
    if targetsum == 0:
        return p
    for num in array:
        rem = targetsum - num
        res = howsum(rem, array)
        if res is not None:
            p.append(num)
            memo[targetsum] = p
            return memo[targetsum]
    memo[targetsum] = None
    return memo[targetsum]

print(howsum(300, [7, 14]))
