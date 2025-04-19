def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	row_len = len(vectors)
    col_len = len(vectors[0])

    # calculating mean of every feature vector
    mean_of_vectors = [(sum(row)/col_len) for row in vectors]
    
    # calculating mean deviation of every instance in each feature
    mean_dev_of_vectors = []
    for i, row in enumerate(vectors):
        mean_dev_of_vectors.append([])
        for x in row:
            mean_dev_of_vectors[i].append(x - mean_of_vectors[i])

    # calculating covariance matrix
    cov_matrix = []
    for i in range(row_len):
        cov_matrix.append([])
        for j in range(row_len):
            if i > j:
                cov_matrix[i].append(cov_matrix[j][i])
            else:
                total = 0
                for k in range(col_len):
                    total += mean_dev_of_vectors[i][k] * mean_dev_of_vectors[j][k]
                cov_matrix[i].append(total/(col_len - 1))

	return 