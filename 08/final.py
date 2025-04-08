alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z']

# Combine the list twice to avoid index out of range errors during shifts
alphabet += alphabet

def encrypt(text, shift):
    encrypted_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift
            encrypted_text += alphabet[new_position]
        else:
            
            encrypted_text += letter
    print(f"Encrypted message: {encrypted_text}")

def decrypt(text, shift):
    decrypted_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position - shift
            decrypted_text += alphabet[new_position]
        else:
            decrypted_text += letter
    print(f"Decrypted message: {decrypted_text}")

# Input from user
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Make sure shift stays in 0–25 range
shift = shift % 26

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Invalid input. Please choose 'encode' or 'decode'.")
