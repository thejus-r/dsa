from typing import List
def canConstruct(word: str, bank: List[str], memo={}) -> bool:
    if word in memo: return memo[word]
    if len(word) == 0: return True

    for subStr in bank:
        if word.startswith(subStr):
            newWord = word.removeprefix(subStr)
            memo[newWord] = canConstruct(newWord, bank)
            return memo[newWord]

    memo[word] = False
    return memo[word]


print(canConstruct("abcdef", [ "abc", "def"]))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [ "e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))
