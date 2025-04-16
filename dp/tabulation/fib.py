def fib(n :int) -> int:
    table = [0] * (n + 1)
    table[1] = 1

    for i in range (len(table)):
        if i+1 < len(table): table[i + 1] += table[i]
        if i+2 < len(table): table[i + 2] += table[i]

    return table[n]

print(fib(6)) #8
print(fib(7)) #13
print(fib(50)) #12586269025
