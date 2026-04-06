def is_armstrong(n):
    digits = len(str(n))
    return n == sum(int(d)**digits for d in str(n))

print(is_armstrong(153))