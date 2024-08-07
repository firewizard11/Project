map = {
    'a':'.-',
    'b':'-...',
    'c':'-.-.',
    'd':'-..',
    'e':'.',
    'f':'..-.',
    'g':'--.',
    'h':'....',
    'i':'..',
    'j':'.---',
    'k':'-.-',
    'l':'.-..',
    'm':'--',
    'n':'-.',
    'o':'---',
    'p':'.--.',
    'q':'--.-',
    'r':'.-.',
    's':'...',
    't':'-',
    'u':'..-',
    'v':'...-',
    'w':'.--',
    'x':'-..-',
    'y':'-.--',
    'z':'--..'
}

def translate_to_morse(text: str) -> str:
    morse = ''
    
    for c in text.lower():
        if c == ' ':
            morse += '/'
        else:
            morse += map[c] + ' '
    
    return morse

def transelate_from_morse(morse: str) -> str:
    text = ''
    morse_letters = morse.split('/')
    pass
    

if __name__ == '__main__':
    test_text = 'bobby'
    text_to_morse = translate_to_morse(test_text)

    print(text_to_morse)