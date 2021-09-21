def grid_traveller(l, memo={}):
    if l in memo.keys():
        return memo[l]
    a,b = l
    m = (b,a)
    if m in memo.keys():
        return memo[m]
    l = list(l)
    print(l)
    if l[0] == 0 or l[1] == 0:
        return 0
    if l == [1,1]:
        return 1
    ld = []
    lr = []
    ld.append(l[0] - 1)
    ld.append(l[1])
    lr.append(l[0])
    lr.append(l[1] - 1)
    memo[tuple(l)] = grid_traveller(tuple(ld), memo) + grid_traveller(tuple(lr), memo)
    return memo[tuple(l)]

grid_axes = (10,10)
res = grid_traveller(grid_axes)
print ("Number of ways we can travel in a %s grid: %s"%(grid_axes, res))