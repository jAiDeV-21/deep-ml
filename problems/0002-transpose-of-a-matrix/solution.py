def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    row_len_a = len(a)
    col_len_a = len(a[0])
    
    b = []
    for row in range(col_len_a):
        b.append([])
        for col in range(row_len_a):
            b[row].append(a[col][row])

	return b