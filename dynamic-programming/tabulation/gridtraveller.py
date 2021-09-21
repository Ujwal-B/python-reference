def gridtraveller(m,n):
    table = [[0 for i in range(0, n+1)] for i in range(0, m+1)]
    printtable(table)
    table[1][1] = 1
    printtable(table)
    for i in range(0, m+1):
        for j in range(0, n+1):
            if j+1 <= n:
                table[i][j+1] += table[i][j]
            if i+1 <= m:
                table[i+1][j] += table[i][j]
    printtable(table)
    return table[m][n]
        

def printtable(table):
    for row in table:
        print(row)



print(gridtraveller(3,2))