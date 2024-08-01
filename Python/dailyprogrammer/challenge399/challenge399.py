#https://www.reddit.com/r/dailyprogrammer/comments/onfehl/20210719_challenge_399_easy_letter_value_sum/

def lettersum(string: str) -> int:
    #Create mapping of alphabet to number
    var = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = {'': 0}
    for i, letter in enumerate(var):
        alphabet[letter] = i + 1

    #Find total of string
    total = 0
    for char in string:
        total += alphabet[char]

    return total


if __name__ == '__main__':
    print(lettersum(""))
    print(lettersum("a"))
    print(lettersum("z"))
    print(lettersum("cab"))
    print(lettersum("excellent"))
    print(lettersum("microspectrophotometries"))
