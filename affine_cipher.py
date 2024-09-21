# affine_cipher.py

def gcd(a, b):
    """Tính UCLN của a và b"""
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    """Tìm nghịch đảo của a mod m"""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(plain_text, a, b):
    """Mã hóa văn bản bằng Affine Cipher"""
    if gcd(a, 26) != 1:
        raise ValueError("a và 26 phải là số nguyên tố cùng nhau.")
    
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            char = char.upper()
            cipher_text += chr(((a * (ord(char) - 65) + b) % 26) + 65)
        else:
            cipher_text += char
    return cipher_text

def affine_decrypt(cipher_text, a, b):
    """Giải mã văn bản bằng Affine Cipher"""
    if gcd(a, 26) != 1:
        raise ValueError("a và 26 phải là số nguyên tố cùng nhau.")
    
    a_inv = mod_inverse(a, 26)
    plain_text = ""
    for char in cipher_text:
        if char.isalpha():
            char = char.upper()
            plain_text += chr(((a_inv * ((ord(char) - 65) - b)) % 26) + 65)
        else:
            plain_text += char
    return plain_text
