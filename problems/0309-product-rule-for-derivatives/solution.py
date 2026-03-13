import numpy as np


def get_degree_of_function(fn):
    return len(fn)


def polynomial_derivative(fn):
    degree_fn = get_degree_of_function(fn)
    d_f = fn[:]
    for d in range(degree_fn):
        d_f[d] *= d
    return d_f[1:]


def remove_trailing_zeros(nums: list) -> list:
    ptr = -1
    while len(nums) > 0 and not nums[ptr]:
        nums.pop()

    return nums


def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    degree_f = get_degree_of_function(f_coeffs)
    degree_g = get_degree_of_function(g_coeffs)

    if degree_g < degree_f:
        f_coeffs, g_coeffs = g_coeffs, f_coeffs

    f_prime = polynomial_derivative(f_coeffs)
    g_prime = polynomial_derivative(g_coeffs)

    f_prime_g = [0.0] * (degree_f + degree_g)
    g_prime_f = [0.0] * (degree_f + degree_g)

    for i, val_f_prime in enumerate(f_prime):
        for j, val_g in enumerate(g_coeffs):
            f_prime_g[i + j] += val_f_prime * val_g

    for i, val_f in enumerate(f_coeffs):
        for j, val_g_prime in enumerate(g_prime):
            g_prime_f[i + j] += val_f * val_g_prime

    f_prime_g_prime = [
        round(val_f_prime_g + val_g_prime_f, 4)
        for (val_f_prime_g, val_g_prime_f) in zip(f_prime_g, g_prime_f)
    ]

    f_prime_g_prime = remove_trailing_zeros(f_prime_g_prime)

    return f_prime_g_prime if f_prime_g_prime else [0.0]