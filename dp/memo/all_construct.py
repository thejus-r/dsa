from typing import List
def allConstruct(target: str, wordBank: List[str]):
    if len(target) == 0: return [[]]

    result = []

    for word in wordBank:
        if (target.startswith(word)):
            suffix = target.removeprefix(word)
            newTarget = allConstruct(suffix, wordBank)
            result.append(newTarget)

    return result

print(allConstruct("abcdef", ["ab", "cd", "ef", "abc", "def", "cdef" , "f"]))
