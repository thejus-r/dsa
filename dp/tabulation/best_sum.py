from typing import List
def bestSum(target: int, numbers: List[int]) -> List[int] | None:
    table: List = [None] * (target + 1)
    table[0] = []

    for i in range (target + 1):
        if table[i] != None:
            for n in numbers:
                if i + n < target + 1:
                    if table[i + n] != None:
                        continue
                    else:
                        table[i + n] = table[i] + [n]

    return table[target]

print(bestSum(8, [2, 5, 3])) # [3, 5]
print(bestSum(9, [1, 3, 2, 5, 4, 9])) # [9]
print(bestSum(9, [3, 1])) # [3, 3, 3]
print(bestSum(9, [4, 2])) # None
