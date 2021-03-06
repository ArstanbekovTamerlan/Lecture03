def is_prime(N):
    N += 1
    A = [True] * N
    A[0] = A[1] = False
    for k in range(2, int(N**0.5)):
        if A[k]:
            for m in range(2*k, N, k):
                A[m] = False
    return [k for k in range(N) if A[k]]


while True:
    try:
        N = int(input("Введите целое число N: "))
        print("Простые числа от 2 до N:", *is_prime(N))
        exit(0)
    except (TypeError, ValueError) as e:
        print("Что-то сломалось, введите число заново!", e)