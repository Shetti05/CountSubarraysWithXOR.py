def rotate(matrix):
    n = len(matrix)
    matrix[:] = list(zip(*matrix[::-1]))