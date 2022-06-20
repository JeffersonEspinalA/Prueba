def fibonacci_dp(n, aux = {0: 0, 1: 1}):
    if n in aux:
        return aux[n]
    aux[n] = fibonacci_dp(n - 1, aux) + fibonacci_dp(n - 2, aux)
    return aux[n]


print(fibonacci_dp(10))