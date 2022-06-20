def fibiterative(n):
    fib = [0,1]
    for i in range(2, n + 1):
        aux = fib[i-1] + fib[i-2]
        fib.append(aux)
    return fib

print(fibiterative(10))