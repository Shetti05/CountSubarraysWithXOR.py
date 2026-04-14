def find_missing(arr, n):
    return n*(n+1)//2 - sum(arr)

print(find_missing([1,2,4,5], 5))