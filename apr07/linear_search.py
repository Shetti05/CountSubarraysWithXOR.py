def search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

print(search([1,3,5,7], 5))