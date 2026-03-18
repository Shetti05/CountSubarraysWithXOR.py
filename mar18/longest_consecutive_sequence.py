def longest_consecutive(nums):
    s = set(nums)
    longest = 0

    for n in s:
        if n - 1 not in s:
            curr = n
            count = 1

            while curr + 1 in s:
                curr += 1
                count += 1

            longest = max(longest, count)

    return longest


nums = [100, 4, 200, 1, 3, 2]
print("Longest Sequence:", longest_consecutive(nums))