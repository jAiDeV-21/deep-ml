def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    row_len = len(matrix)
    col_len = len(matrix[0])

    means = []

    if mode == 'row':
        for row in matrix:
            sum = 0
            for ele in row:
                sum += ele
            means.append(float(sum)/row_len)
    else:
        for col in range(col_len):
            sum = 0
            for row in range(row_len):
                sum += matrix[row][col]
            means.append(float(sum)/col_len)
	return means