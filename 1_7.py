def set_zeros(matrix):
    row_has_zero = len(matrix) * [False]
    column_has_zero = len(matrix[0]) * [False]

    for row in xrange(len(matrix)):
        for column, value in enumerate(matrix[row]):
            if value == 0:
                column_has_zero[column] = True
                row_has_zero[row] = True

    for row in xrange(len(matrix)):
        for column in xrange(len(matrix[row])):
            if row_has_zero[row] or column_has_zero[column]:
                matrix[row][column] = 0
