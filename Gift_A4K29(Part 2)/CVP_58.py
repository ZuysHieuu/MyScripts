def check_prime(n):
    if (n <= 1):
        return "khong la so nguyen to."
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if (n % i == 0):
                return "khong la so nguyen to."
        return "la so nguyen to."
n = int(input())
print(n, check_prime(n))