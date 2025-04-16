def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    row_len = len(matrix)
    col_len = len(matrix[0])
    result = []

    for row in range(row_len):
        result.append([])
        for col in range(col_len):
            result[row].append(scalar * matrix[row][col])

	return result