def next_greater(arr):
    stack = []
    
    for num in arr:
        while stack and stack[-1] < num:
            print(stack.pop(), "->", num)
        stack.append(num)

    while stack:
        print(stack.pop(), "-> -1")


arr = [4, 5, 2, 25]
next_greater(arr)