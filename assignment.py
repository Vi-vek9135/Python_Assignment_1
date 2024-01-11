# Function to encrypt a message using a key
def encrypt(message, key):

  # To store encrypted message  
  encrypted_message = ""

  # Iterate through each character in the message
  for char in message:
      
    # To shift the character's ASCII value by the key
    new_char_code = ord(char) + key

    # To wrap around if the shifted value goes beyond the printable ASCII range
    new_char_code = (new_char_code - 32) % 95 + 32

    # To convert the shifted value back to a character and append to the encrypted message
    encrypted_message += chr(new_char_code)

  return encrypted_message



# Function to decrypt an encrypted message using a key
def decrypt(message, key):

  # To store decrypted message  
  decrypted_message = ""

  # Iterate through each character in the message
  for char in message:
      
    # To shift the character's ASCII value backward by the key
    new_char_code = ord(char) - key

    # To wrap around if the shifted value goes beyond the printable ASCII range
    new_char_code = (new_char_code - 32) % 95 + 32

    # To convert the shifted value back to a character and append to the decrypted message
    decrypted_message += chr(new_char_code)

  return decrypted_message




# Taking user inputs for message, key, and mode
message = input("Enter the message: ")
key = int(input("Enter the key (an integer): "))
mode = input("Choose mode (encrypt/decrypt): ")

# To perform encryption or decryption based on the user's choice
if mode == "encrypt":
  result = encrypt(message, key)
  print("Encrypted message:", result)
elif mode == "decrypt":
  result = decrypt(message, key)
  print("Decrypted message:", result)
else:
  print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
  exit()

