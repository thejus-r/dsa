from typing import List
def allConstruct(target: str, wordBank: List[str]) -> List:
    length = len(target)
    table: List[List]= [[]] * (length + 1)
    table[0] = [[]] # seed state

    for i in range (length + 1):
        if len(table[i]) != 0:
            for word in wordBank:
                if (target[i: i + len(word)] == word):
                    for comb in table[i]:
                        print("Found 1", comb)

    return table[length]

print(allConstruct("abcdef", ["abc", "ab", "def", "c", "cd", "ef"]))
