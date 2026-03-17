import heapq

def kth_smallest(nums, k):
    return heapq.nsmallest(k, nums)[-1]