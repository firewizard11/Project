from random import randrange


def generate_password(length: int) -> str:
    password = ''
    
    for i in range(length):
        password += chr(randrange(33, 127))

    return password


if __name__ == '__main__':
    num_pass = int(input('How many passwords would you like: '))
    length = int(input('How long would you like your passwords: '))

    print('Your passwords are:')
    for i in range(num_pass):
        print('- ', generate_password(length))
    
    input('Click a key to close: ')