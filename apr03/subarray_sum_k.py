def subarray_sum(nums, k):
    count = 0
    prefix = {0:1}
    s = 0

    for n in nums:
        s += n
        if s-k in prefix:
            count += prefix[s-k]
        prefix[s] = prefix.get(s,0)+1
    return count