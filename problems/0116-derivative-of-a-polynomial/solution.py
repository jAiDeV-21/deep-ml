def poly_term_derivative(c: float, x: float, n: float) -> float:
    ans = c * n * pow(x, n - 1)
    return ans