def factorial(n):
    if n < 0:
        print("Errol")
    elif n == 0 or n == 1:
        print(1)
    else:
        res = 1
        for i in range(2, n + 1):
            res *= i
        print(f"Luy thua cua {n} la: {res}.")
n = int(input())
factorial(n)