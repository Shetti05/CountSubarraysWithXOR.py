arr = [10, 20, 5, 8]
first = second = float('-inf')

for n in arr:
    if n > first:
        second = first
        first = n
    elif n > second and n != first:
        second = n

print(second)