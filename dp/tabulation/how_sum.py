from typing import List
def howSum(target: int, number: List[int]) -> List[int]:
    table: List = [None] * (target+1)
    table[0] = []

    for i in range (target + 1):
        for n in number:
            if table[i] != None and (i + n) < target + 1:
                table[i + n] = table[i] + [n]


    return table[target] != None

print(howSum(7, [2, 3, 5])) # True
print(howSum(7, [3, 5])) # False
print(howSum(0, [3, 5])) # True
print(howSum(300, [7, 14])) # False
