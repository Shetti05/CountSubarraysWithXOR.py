# File: median_two_sorted.py
def findMedianSortedArrays(a, b):
    nums = sorted(a + b)
    n = len(nums)
    if n % 2:
        return nums[n//2]
    return (nums[n//2 - 1] + nums[n//2]) / 2

print(findMedianSortedArrays([1,3], [2]))