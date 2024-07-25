def sum_square_dif(n):
    sum_of_squares = sum([x ** 2 for x in range(1, n + 1)])
    square_of_sum = sum([x for x in range(1, n + 1)]) ** 2
    return abs(sum_of_squares - square_of_sum)

if __name__ == '__main__':
    n = 100
    print(sum_square_dif(n))
    input('Click Enter to End')