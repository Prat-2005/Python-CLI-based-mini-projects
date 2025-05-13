# Text Encrpytion Generator

import random

alphabets = "abcdefghijklmnopqrstuvwxyz"
shift = random.randint(5, 10)
encrypted_text = ""

try:
    text = input("Enter text (only letters, no spaces or special characters): ")
    
    if not text.isalpha():
        raise ValueError("Text must contain only letters (a-z or A-Z), no numbers or special characters.")
    
    for ch in text:
        is_upper = ch.isupper()
        ch = ch.lower()
        index = alphabets.find(ch)
        new_index = (index + shift) % len(alphabets) # this logic works better. Remember, whenever you want to startover anything used "%(modulo operator)".
        encrypted_char = alphabets[new_index]
        if is_upper:
            encrypted_char = encrypted_char.upper()
        encrypted_text += encrypted_char

    print(f"Encrypted text: {encrypted_text}")
    print(f"Encryption shift key: {shift}")

except ValueError as e:
    print(f"ERROR! {e}")
