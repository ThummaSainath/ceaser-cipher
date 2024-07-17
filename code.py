def encrypt_decrypt(text, key, mode):
    result = ""
    
    for ch in text:
        if ch.isalnum():
            if ch.islower():
                if mode == '1':  # Encryption
                    result += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
                elif mode == '2':  # Decryption
                    result += chr((ord(ch) - ord('a') - key + 26) % 26 + ord('a'))
            elif ch.isupper():
                if mode == '1':  # Encryption
                    result += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
                elif mode == '2':  # Decryption
                    result += chr((ord(ch) - ord('A') - key + 26) % 26 + ord('A'))
            elif ch.isdigit():
                if mode == '1':  # Encryption
                    result += chr((ord(ch) - ord('0') + key) % 10 + ord('0'))
                elif mode == '2':  # Decryption
                    result += chr((ord(ch) - ord('0') - key + 10) % 10 + ord('0'))
        else:
            print("Invalid Message")
            return None
    
    return result

if __name__ == "__main__":
    text = input("Enter a message to encrypt or decrypt: ")
    key = int(input("Enter the key: "))
    mode = input("Enter '1' for Encryption and '2' for Decryption: ")
    
    if mode not in ['1', '2']:
        print("Invalid mode selected.")
    else:
        result = encrypt_decrypt(text, key, mode)
        if result:
            if mode == '1':
                print("Encrypted message:", result)
            elif mode == '2':
                print("Decrypted message:", result)
