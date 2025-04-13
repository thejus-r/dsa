from typing import List

def canSum(targetSum: int, numbers: List[int], memo = {}) -> bool:
    if targetSum in memo: return memo[targetSum]
    if (targetSum == 0): return True

    if (targetSum < 0): return False

    for num in numbers:
        remainder = targetSum - num
        if (canSum(remainder, numbers, memo) == True):
            memo[targetSum] = True
            return memo[targetSum]

    memo[targetSum] = False
    return memo[targetSum]

print(canSum(300, [7,14]))
