#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    A function that computes the square
    values of all integers of a matrix

    Args:
        matrix (list) - A 2-dimensional array

    Return:
        A new matrix, of the same size as matrix
        and each value should be the square of
        the value of the input
    """
    if not matrix:
        pass
    else:
        # square = lambda x: x ** 2
        return list(list(map(lambda x: x ** 2, number)) for number in matrix)
