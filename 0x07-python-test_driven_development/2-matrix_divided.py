#!/usr/bin/python3
"""matrix_divided - divide each element"""


def matrix_divided(matrix, div):
    """matrix_divided

    Arguments:
        matrix {list} -- matrix must be a list of lists [[],[],...]
        div {int, float} -- div must be a number != 0

    Raises:
        TypeError: div must be a number
        ZeroDivisionError: division by zero
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: matrix must be a matrix (list of lists) of integers/floats
    """
    m_error = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    try:
        row = matrix[1][0]
    except:
        raise TypeError(m_error)

    new_matrix = []
    length = len(matrix[0])

    for row in matrix:
        new_row = []
        if type(row) is not list:
            raise TypeError(m_error)
        elif length != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if type(element) not in (int, float):
                raise TypeError(m_error)
            new_row.append(round(element/div, 2))
        new_matrix.append(new_row)
    return(new_matrix)
