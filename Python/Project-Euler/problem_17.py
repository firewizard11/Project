from num2words import num2words


def number_letter_count(n):
    words = []
    total_letters = 0

    for i in range(1, n + 1):
        words.append(num2words(i))

    for word in words:
        word = word.replace(' ', '').replace('-', '')
        total_letters += len(word)

    return total_letters
    

if __name__ == '__main__':
    n = 1000
    print(number_letter_count(n))