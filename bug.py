def function(x):
    if x == 0:
        return 1
    else:
        return x * function(x-1)

print(function(5)) #This will work perfectly
print(function(-1)) #This will cause a RecursionError