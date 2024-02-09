user_input = input("Insert your text to encrtypt: ")
user_shift = input("Provide the encryption number: ")
text = str(user_input)
shift = int(user_shift)

def decrypt_python():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in text.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + shift) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('normal text:', text)
    print('encrypted text:', encrypted_text)

decrypt_python()