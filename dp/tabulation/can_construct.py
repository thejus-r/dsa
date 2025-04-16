from typing import List
def canConstruct(target: str, wordBank: List[str]) -> bool:
    length = len(target)
    table = [False] * (length + 1)
    table[0] = True

    for i in range (length):
        if table[i]:
            for word in wordBank:
                if target[i:i + len(word)] == word:
                    table[i + len(word)] = True

    print(table)
    return table[length]

print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # True
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # False
