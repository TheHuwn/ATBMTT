# shift_cipher.py

special_chars = " @_."  
special_chars_length = len(special_chars)

def shift_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr(((ord(char) - ascii_offset + key) % 26) + ascii_offset)
            encrypted_text += encrypted_char
        elif char in special_chars:
            index = special_chars.index(char)
            new_index = (index + key) % special_chars_length
            encrypted_text += special_chars[new_index]
        else:
            encrypted_text += char
    return encrypted_text

def shift_decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted_char = chr(((ord(char) - ascii_offset - key) % 26) + ascii_offset)
            decrypted_text += decrypted_char
        elif char in special_chars:
            index = special_chars.index(char)
            new_index = (index - key) % special_chars_length
            decrypted_text += special_chars[new_index]
        else:
            decrypted_text += char
    return decrypted_text
