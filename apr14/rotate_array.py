def rotate(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k]

print(rotate([1,2,3,4,5], 2))