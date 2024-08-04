alphabet = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
length = len(alphabet)


def encrypt(plaintext: str, key: int) -> str:
    ciphertext = ''
    
    for c in plaintext:
        if c == ' ':
            ciphertext += ' '
        else: 
            ciphertext += alphabet[(alphabet.index(c) + key) % (length - 1)]

    return ciphertext


def decrypt(ciphertext: str, key: int) -> str:
    plaintext = ''

    for c in ciphertext:
        if c == ' ':
            plaintext += ' '
        else:
            plaintext += alphabet[(alphabet.index(c) - key) % (length - 1)]

    return plaintext

if __name__ == '__main__':
    choice = input("""Welcome to the Caeser Cipher tool!
1. Encrypt
2. Decrypt
Please Enter your choice: """)

    string = input('Please Enter your text (a-z,A-Z): ')
    key = int(input('Please Enter your key (A number please): '))

    if choice == '1':
        print(encrypt(string, key))
    elif choice == '2':
        print(decrypt(string, key))

    input('')