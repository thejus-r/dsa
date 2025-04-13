from typing import List
def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:

    def walk(m: int, n:int, memo = {}):
        key = str(m) + "," + str(n)
        if key in memo: return memo[key]
        if (m == 0 and n == 0 and obstacleGrid[m][n] == 0): return 1
        if (m < 0 or n < 0 or obstacleGrid[m][n] == 1) : return 0

        memo[key] = walk(m, n-1, memo) + walk(m-1, n, memo)
        return memo[key]

    m, n = len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1
    return walk(m, n)

print(uniquePathsWithObstacles([[0,1],[0,0]]))
