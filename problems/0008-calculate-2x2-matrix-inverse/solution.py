def determinant(matrix: list[list[float]]) -> float:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.

    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]

    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    det_matrix = determinant(matrix)
    if not det_matrix:
        return None

    inverse_matrix = [
        [matrix[1][1] / det_matrix, -matrix[0][1] / det_matrix],
        [-matrix[1][0] / det_matrix, matrix[0][0] / det_matrix],
    ]

    return inverse_matrix