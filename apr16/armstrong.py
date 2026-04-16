num = 153
sum = 0
temp = num

while temp > 0:
    d = temp % 10
    sum += d**3
    temp //= 10

print(sum == num)