def daily_temperatures(temps):
    res = [0]*len(temps)
    stack = []

    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            idx = stack.pop()
            res[idx] = i - idx
        stack.append(i)

    return res

print(daily_temperatures([73,74,75,71,69,72,76,73]))