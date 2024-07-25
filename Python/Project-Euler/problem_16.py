

def power_digit_sum(exp):
    num = 2 ** exp
    digits = [int(char) for char in str(num)]
    return sum(digits)

print(power_digit_sum(1000))
input('Click Enter to End')