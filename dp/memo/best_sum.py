from typing import List
def bestSum(targetSum :int, numbers: List[int], memo={}) -> List[int] | None:

    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None

    shortestCombination = None
    for num in numbers:
       reminder = targetSum - num
       reminderCombination = bestSum(reminder, numbers)
       if (reminderCombination != None):
           combination = reminderCombination + [num]
           if (shortestCombination == None or len(combination) < len(shortestCombination)):
               shortestCombination = combination

    memo[targetSum] = shortestCombination
    return memo[targetSum]



print(bestSum(300, [1,2,3,4,5,100,150, 25, 300]))
