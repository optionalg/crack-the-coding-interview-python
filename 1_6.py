def rotate(matrix):
    n = len(matrix)

    for layer in xrange(n / 2):
        for i in xrange(0, n - 1 - layer * 2):
            top = matrix[layer][n - 1 - i - layer]

            # Left to Top
            matrix[layer][n - 1 - i - layer] = matrix[layer + i][layer]

            # Bottom to Left
            matrix[layer + i][layer] = matrix[n - 1 - layer][layer + i]

            # Right to Bottom
            matrix[n - 1 - layer][layer + i] = matrix[n - 1 - layer - i][n - 1 - layer]

            # Top to Right
            matrix[n - 1 - layer - i][n - 1 - layer] = top
