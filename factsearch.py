def fact(x):
    if x != 1:
        return fact(x-1)*x
    return 1

print(fact(4))
print(fact(1))
print(fact(10))