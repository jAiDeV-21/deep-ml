import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	row_len_a = len(a)
	col_len_a = len(a[0])

	reshaped_matrix = []


	if len(new_shape) == 1 and row_len_a * col_len_a == new_shape[0]:
		for row in a:
			for i in range(col_len_a):
				reshaped_matrix.append(row[i])
	elif row_len_a * col_len_a == new_shape[0] * new_shape[1]:
		row_ptr, col_ptr = 0, 0
		for row in range(new_shape[0]):
			reshaped_matrix.append([])
			for col in range(new_shape[1]):
				if col_ptr == col_len_a:
					col_ptr = 0
					row_ptr += 1

				reshaped_matrix[row].append(a[row_ptr][col_ptr])
				col_ptr += 1
			if col_ptr == col_len_a:
					col_ptr = 0
					row_ptr += 1
			
	return reshaped_matrix