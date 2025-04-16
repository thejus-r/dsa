
def gridTraveller(m: int, n:int, memo = {}):
    key = str(m) + "," + str(n)
    if key in memo: return memo[key]

    if (m == 1 and n == 1): return 1
    if (m == 0 or n == 0): return 0

    memo[key] = gridTraveller(m - 1, n, memo) + gridTraveller(m, n - 1, memo)
    return memo[key]

def main():
    print(gridTraveller(1, 1))
    print(gridTraveller(2, 3))
    print(gridTraveller(18, 18))


main()
