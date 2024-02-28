alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  #Create a var for the ending string
  end_text = ""

  #if the user chooses decode
  if cipher_direction == "decode":

    #set the shift amount to minus equal the value entered by the user
    shift_amount *= -1

  #for a char in the starting text  
  for char in start_text:
    #if the character is in the alphabet
    if char in alphabet:
      
      #the position of the letter is the position in our alphabet
      position = alphabet.index(char)

      #the new position is the position plus the shift
      new_position = position + shift_amount

      #the end text is now the adding each character at the new position.
      end_text += alphabet[new_position]
    else:
      end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Peace")