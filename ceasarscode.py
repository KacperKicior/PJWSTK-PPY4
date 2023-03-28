def caesar_cipher(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_message = ''
    for letter in message:
        if letter.lower() in alphabet:
            shifted_index = (alphabet.index(letter.lower()) + key) % len(alphabet)
            if letter.isupper():
                encrypted_message += alphabet[shifted_index].upper()
            else:
                encrypted_message += alphabet[shifted_index]
        else:
            encrypted_message += letter
    print(encrypted_message)


msg = input("Podaj wiadomosc: ")
inputkey = int(input("Podaj klucz: "))

caesar_cipher(msg, inputkey)
