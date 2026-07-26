# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
# TODO-2: What happens if the user enters a number/symbol/space?
value= True
while(value):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))


        # TODO-3: Can you figure out a way to restart the cipher program?


        def encrypt(original_text, shift_amount):
            cipher_text = ""
            for letter in original_text:
              if letter not in alphabet:
                cipher_text += letter
              else:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                cipher_text += alphabet[shifted_position]
            print(f"Here is the encoded result: {cipher_text}")


        def decrypt(original_text, shift_amount):
            cipher_text = ""
            for letter in original_text:
                shifted_position = alphabet.index(letter) - shift_amount
                shifted_position %= len(alphabet)
                cipher_text += alphabet[shifted_position]
            print(f"Here is the decoded result: {cipher_text}")


        def caesar(direction):
            if direction == "encode":
                encrypt(original_text=text, shift_amount=shift)
            elif direction == "decode":
                decrypt(original_text=text, shift_amount=shift)
            else:
                print("Please enter 'encode' or 'decode' your input is incorrect.")
        caesar(direction)
condition_var=input("do you want to play again?(y/n)\n").lower()
if condition_var == "y":
    value = True
elif condition_var == "n":
    value = False
else:
    print("Please enter correct input.")

