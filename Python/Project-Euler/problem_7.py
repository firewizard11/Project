import math


def prime_test(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def prime_list(length):
    primes = []
    num = 2
    while len(primes) < length:
        if prime_test(num):
            primes.append(num)
            num += 1
        else:
            num += 1
    return primes


if __name__ == '__main__':
    length = 10001
    print(prime_list(length)[-1])
    input('Click Enter to End')