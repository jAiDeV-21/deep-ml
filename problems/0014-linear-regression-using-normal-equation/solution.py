import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X = np.array(X)
    y = np.array(y)

    theta = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, y.T))
    theta = np.round(theta, decimals=4)
	return theta.tolist()