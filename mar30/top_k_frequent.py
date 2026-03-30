from collections import Counter

def top_k_frequent(nums, k):
    return [item for item, _ in Counter(nums).most_common(k)]

print(top_k_frequent([1,1,1,2,2,3], 2))