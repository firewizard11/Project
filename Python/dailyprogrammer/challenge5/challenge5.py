if __name__ == '__main__':
    if input('Please enter your username: ') == 'root':
        if input('Please enter your password: ') == '123':
            print('You are authenticated!!!!')
        else:
            print('Incorrect Password!')
    else:
        print('Incorrect Username!')