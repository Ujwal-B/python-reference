def cansum(sum, array, memo = {}):
    print(sum)
    if sum in memo.keys():
        return memo[sum]
    
    if sum < 0:
        return False
    if sum == 0:
        return True
    # for i in range(0, len(array)):
    for num in array:
        if cansum(sum - num, array, memo) is True:
            memo[sum] = True
            return True
    memo[sum] = False
    return False

print(cansum(300,[9]))