def function(x):
    if x < 0:
        return "Factorial is not defined for negative numbers"
    elif x == 0:
        return 1
    else:
        return x * function(x-1)

print(function(5))
print(function(-1))