def bestsum(targetsum, array, memo={}):
    if targetsum in memo.keys():
        return memo[targetsum]
    if targetsum == 0:
        return []
    if targetsum < 0:
        return None
    shortestcombination = None
    for num in array:
        remainder = targetsum - num
        remaindercombination = bestsum(remainder, array, memo)
        if remaindercombination is not None:
            combination = remaindercombination
            combination.append(num)
            if shortestcombination is None or len(combination) < len(shortestcombination):
                shortestcombination = combination
    memo[targetsum] = shortestcombination
    return shortestcombination

print(bestsum(7, [5,3,4]))
print(bestsum(8, [2,3,5]))
print(bestsum(8, [1,4,5]))
# something is wrong, check it out later
print(bestsum(100, [1,2,5,25]))