def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	row_len_a = len(a)
	col_len_a = len(a[0])

	row_len_b = len(b)
	col_len_b = 1

	result = None

	if col_len_a == row_len_b:
		result = [0] * row_len_a
		for row in range(row_len_a):
			for col in range(col_len_a):
				result[row] += a[row][col] * b[col]
	else:
		result = -1

	return result


