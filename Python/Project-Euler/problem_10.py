from problem_7 import prime_test


def prime_list(max):
    primes = []
    for n in range(2, max):
        if prime_test(n):
            primes.append(n)
    return primes


if __name__ == '__main__':
    max = 2000000
    primes = prime_list(max)
    print(sum(primes))
    input('Click Enter to End')
