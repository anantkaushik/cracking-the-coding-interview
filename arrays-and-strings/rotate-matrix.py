"""
Given an image represented by an N * N matrix, where each pixel in the image is 4 bytes, write a method to rotate the
image by 90 degrees. Can you do this in place?
"""
def rotate(matrix):
    l = len(matrix)
    if l == 0 or l != len(matrix[0]):
        return False
    for layer in range(l//2):
        first,last = layer, l-1-layer
        for i in range(first,last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last-offset][first]
            matrix[last-offset][first] = matrix[last][last-offset]
            matrix[last][last-offset] = matrix[i][last]
            matrix[i][last] = top
    return True