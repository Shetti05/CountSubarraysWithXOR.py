arr = [2,3,10,6,4,8,1]

max_diff = arr[1] - arr[0]

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        max_diff = max(max_diff, arr[j]-arr[i])

print(max_diff)