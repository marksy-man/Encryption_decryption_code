def decrypt_caesar(ciphertext):
    plaintext = ""
    for shift in range(26):
        decrypted_text = ""
        for char in ciphertext:
            if char.isalpha():
                shifted = ord(char) - shift
                if char.islower():
                    if shifted < ord('a'):
                        shifted += 26
                    elif shifted > ord('z'):
                        shifted -= 26
                elif char.isupper():
                    if shifted < ord('A'):
                        shifted += 26
                    elif shifted > ord('Z'):
                        shifted -= 26
                decrypted_text += chr(shifted)
            else:
                decrypted_text += char
        plaintext += f"Shift {shift}: {decrypted_text}\n"
    return plaintext

def main():
    ciphertext = input("Enter the ciphertext: ")
    decrypted_results = decrypt_caesar(ciphertext)
    print("Possible Decrypted Texts:")
    print(decrypted_results)

if __name__ == "__main__":
    main()
