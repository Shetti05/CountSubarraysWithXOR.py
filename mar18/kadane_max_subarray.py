def max_subarray(arr):
    max_sum = curr = arr[0]

    for i in arr[1:]:
        curr = max(i, curr + i)
        max_sum = max(max_sum, curr)

    return max_sum


arr = [-2,1,-3,4,-1,2,1,-5,4]
print("Max Sum:", max_subarray(arr))