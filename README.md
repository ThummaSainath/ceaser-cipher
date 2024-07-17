This Python program encrypts or decrypts a given alphanumeric message using a simple Caesar cipher. The Caesar cipher is a type of substitution cipher in which each character in the plaintext is shifted a certain number of places down or up the alphabet based on a key. The same key is used for both encryption and decryption, but the operation differs slightly between the two processes.

**Detailed Breakdown:**
**Function Definition:**

The program defines a function encrypt_decrypt(text, key, mode) that handles both encryption and decryption based on the mode specified.

The function iterates over each character in the input text and processes it according to whether it is a lowercase letter, an uppercase letter, or a digit.

**Character Processing:**

Lowercase Letters:

For encryption (mode == '1'), the character is shifted forward by the key value.

For decryption (mode == '2'), the character is shifted backward by the key value.

**Uppercase Letters:**

Similar to lowercase letters, but the operations are adjusted for the uppercase ASCII range.

**Digits:**
Digits are also shifted forward or backward within their range (0-9).

**Validation:**

The function checks if each character is alphanumeric. 

If a non-alphanumeric character is encountered, an error message is printed, and the function returns None.

**User Input:**

The user is prompted to enter the message they wish to encrypt or decrypt.

The user then provides a key (an integer) which determines the shift in the cipher.

Finally, the user specifies the mode: '1' for encryption or '2' for decryption.

**Main Program Logic:**

The main block of the program checks if the mode input by the user is valid.

It then calls the encrypt_decrypt function with the provided inputs.

The resulting encrypted or decrypted message is printed to the console.
