from typing import List
def countConstruct(target: str, wordBank:List[str], memo={}) -> int:
    count = 0

    if target in memo: return memo[target]

    if (len(target) == 0): return 1
    for word in wordBank:
        if(target.startswith(word)):
            newWord = target.removeprefix(word)
            numWays = countConstruct(newWord, wordBank, memo)
            count += numWays

    memo[target] = count
    return memo[target]


print(countConstruct("abcdef",["abc", "def", "abcd", "ef"]))
print(countConstruct("purple",["purp", "p", "ur","le", "purpl"]))
