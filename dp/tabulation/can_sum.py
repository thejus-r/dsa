from typing import List
def canSum(target: int, numbers:List) -> bool:
    dp = [False] * (target+1)
    dp[0] = True
    i = 0
    while( i < len(dp)):
        if (dp[i] == True):
            for n in numbers:
                nextIndex = i + n
                if nextIndex < len(dp):
                    dp[i + n] = True

        i += 1

    return dp[-1]


print(canSum(7, [2, 3])) # True
print(canSum(0, [2, 3])) # True
print(canSum(7, [9, 5])) # False
print(canSum(7, [3, 4, 5, 7])) # True
