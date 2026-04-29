arr = [2, 4, 6, 8, 10]
key = 8
low, high = 0, len(arr)-1

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        print("Found at", mid)
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Not found")