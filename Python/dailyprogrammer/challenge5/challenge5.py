def read_file(file_name):
    with open(file_name, 'r') as file_read:
        username = file_read.readline().strip()
        password = file_read.readline()
    return (username, password)

if __name__ == '__main__':
    creds = read_file('secret.txt')

    if input('Please enter your username: ') == creds[0]:
        if input('Please enter your password: ') == creds[1]:
            print('You are authenticated!!!!')
        else:
            print('Incorrect Password!')
    else:
        print('Incorrect Username!')

    input('Click Enter to close: ')