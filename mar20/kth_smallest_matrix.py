import heapq

def kthSmallest(matrix, k):
    n = len(matrix)
    heap = [(matrix[i][0], i, 0) for i in range(n)]
    heapq.heapify(heap)
    
    for _ in range(k):
        val, r, c = heapq.heappop(heap)
        if c+1 < n:
            heapq.heappush(heap, (matrix[r][c+1], r, c+1))
    
    return val

print(kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))