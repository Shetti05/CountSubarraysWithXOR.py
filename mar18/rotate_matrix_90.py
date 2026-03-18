def rotate_matrix(mat):
    # Transpose
    mat = list(zip(*mat))

    # Reverse rows
    mat = [list(row[::-1]) for row in mat]

    return mat


matrix = [[1,2,3],[4,5,6],[7,8,9]]

rotated = rotate_matrix(matrix)

for row in rotated:
    print(row)