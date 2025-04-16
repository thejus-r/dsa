from typing import List
def countConstruct(target: str, wordBank: List[str]) -> int:
    length = len(target)
    table = [0] * (length + 1)
    table[0] = 1

    for i in range (length + 1):
        if table[i] != 0:
            for word in wordBank:
                if target[i:i + len(word)] == word:
                    table[i + len(word)] += table[i]

    return table[length]

print(countConstruct("abcdef", ["ab", "abc", "def", "cd", "ef"])) # 2
print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"])) # 2
print(countConstruct("aaa", ["a", "aa", "abc"])) # 3
print(countConstruct("eeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee"])) # 0
