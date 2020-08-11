def fact(x):
    if x == 1:
        return x
    else:
        return x * fact(x - 1)


print((fact(10)))
