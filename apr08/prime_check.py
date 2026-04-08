n = 29
is_prime = True

for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        is_prime = False
        break

print("Prime" if is_prime else "Not Prime")