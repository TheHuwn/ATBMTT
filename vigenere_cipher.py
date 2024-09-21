# vigenere_cipher.py

def vigenere_encrypt(text, key):
    encrypted_text = []
    key = key.upper()
    key_length = len(key)
    key_index = 0

    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            key_char = key[key_index % key_length].upper()
            shift = ord(key_char) - 65
            encrypted_char = chr(((ord(char) - ascii_offset + shift) % 26) + ascii_offset)
            encrypted_text.append(encrypted_char)
            key_index += 1
        else:
            encrypted_text.append(char)

    return ''.join(encrypted_text)

def vigenere_decrypt(text, key):
    decrypted_text = []
    key = key.upper()
    key_length = len(key)
    key_index = 0

    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            key_char = key[key_index % key_length].upper()
            shift = ord(key_char) - 65
            decrypted_char = chr(((ord(char) - ascii_offset - shift) % 26) + ascii_offset)
            decrypted_text.append(decrypted_char)
            key_index += 1
        else:
            decrypted_text.append(char)

    return ''.join(decrypted_text)
