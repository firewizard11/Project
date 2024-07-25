def function():
    m = 2
    while True:
        for n in range(1, m):
            a = (m ** 2) - (n ** 2)
            b = 2 * m * n
            c = (m ** 2) + (n ** 2)
            if (a ** 2) + (b ** 2) == (c ** 2) and a + b + c == 1000:
                return a * b * c
        m += 1
        
print(function())
input('Click Enter')
