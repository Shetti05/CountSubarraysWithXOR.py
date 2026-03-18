def longest(nums):
    num_set = set(nums)
    longest = 0

    for n in nums:
        if n - 1 not in num_set:
            curr = n
            streak = 1

            while curr + 1 in num_set:
                curr += 1
                streak += 1

            longest = max(longest, streak)

    return longest