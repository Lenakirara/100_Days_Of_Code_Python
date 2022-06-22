alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
  # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    # e.g. 
    # plain_text = "hello"
    # shift = 5
    # cipher_text = "mjqqt"
    # print output: "The encoded text is mjqqt"
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    position += shift_amount
    if position > len(alphabet):
      position -= len(alphabet)          
    cipher_text = cipher_text + alphabet[position]
  print(f"The encoded text is {cipher_text}")

# TODO-3: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift_amount):
  #TODO-4: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
  original_text = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    position -= shift_amount
    if position > len(alphabet):
      position += len(alphabet)          
    original_text = original_text + alphabet[position]
  print(f"The decoded text is {original_text}")

# TODO-5: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == 'encode':
  encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
  decrypt(cipher_text=text, shift_amount=shift)
