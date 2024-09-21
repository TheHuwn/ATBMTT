# substitution_cipher.py

import string
import random

def generate_key():
    """Tạo một key ngẫu nhiên cho Substitution Cipher."""
    letters = list(string.ascii_lowercase)
    shuffled = random.sample(letters, len(letters))
    return ''.join(shuffled)

def encrypt(text, key):
    """Mã hóa văn bản bằng Substitution Cipher."""
    alphabet = string.ascii_lowercase
    table = str.maketrans(alphabet, key)
    return text.translate(table)

def decrypt(text, key):
    """Giải mã văn bản bằng Substitution Cipher."""
    alphabet = string.ascii_lowercase
    table = str.maketrans(key, alphabet)
    return text.translate(table)
