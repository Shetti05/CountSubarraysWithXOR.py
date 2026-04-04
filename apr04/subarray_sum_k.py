def subarray_sum(nums, k):
    d = {0:1}
    s = count = 0
    for num in nums:
        s += num
        count += d.get(s-k, 0)
        d[s] = d.get(s,0)+1
    return count