def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)
fact = factorial

print(list(map(fact, filter(lambda n: n % 2, range(6)))))

print([fact(n) for n in range(6) if n % 2])