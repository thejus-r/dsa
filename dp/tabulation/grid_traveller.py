def gridTraveller(m: int, n: int) -> int:
    table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    table[1][1] = 1

    for row in range(0,m + 1):
        for col in range(0,n + 1):
            if col + 1 <= n: table[row][col+1] += table[row][col]
            if row + 1 <= m: table[row+1][col] += table[row][col]

    return table[m][n]


print(gridTraveller(3, 3))
