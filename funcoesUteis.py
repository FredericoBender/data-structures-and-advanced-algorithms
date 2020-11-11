def chao(x):
    """Retorna um int, com valor chão de um número"""
    return int(x//1)

def teto(x):
    """Retorna um int, com valor teto de um número"""
    if x == int(x):
        return int(x)
    return int(x//1 + 1)

def fatorial(x):
    """Retorna o fatorial de um elemento"""
    fat = 1
    for i in range(x):
        fat *= i + 1     
    return fat

def fibonacci(n):
    """Calcula o n'ésimo elemento da sequencia de fibonacci"""
    f0, f1 = 0, 1
    if n == 1: return f0
    elif n == 2: return f1
    for i in range(n-2):
        fib = f0 + f1
        f0 = f1
        f1 = fib
    return fib

fatoriais = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]