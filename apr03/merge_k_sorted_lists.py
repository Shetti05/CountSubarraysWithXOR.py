import heapq

def merge_k_lists(lists):
    heap = []
    for i, l in enumerate(lists):
        if l:
            heapq.heappush(heap, (l[0], i, 0))

    res = []
    while heap:
        val, i, j = heapq.heappop(heap)
        res.append(val)
        if j+1 < len(lists[i]):
            heapq.heappush(heap, (lists[i][j+1], i, j+1))
    return res