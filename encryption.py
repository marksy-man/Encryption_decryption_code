def encrypt(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def main():
    plaintext = input("Enter the plaintext: ")
    shift = int(input("Enter the shift for encryption: "))
    encrypted_text = encrypt(plaintext, shift)
    print("Encrypted Text:", encrypted_text)
    print("Encryption Key (Shift):", shift)

if __name__ == "__main__":
    main()
