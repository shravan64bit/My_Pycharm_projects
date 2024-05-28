alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
def encyrpt(text, shift):
    new = ''
    for letter in text:
        if letter == ' ':
            index = text.index(letter)
            new += text[index]
        else:
            index = alphabet.index(letter) + shift
            if index < 25:
                new += alphabet[index]
            else:
                new_index = index - 26
                new += alphabet[new_index]
    print(f"The encoded text is {new}")


def decrypt(text, shift):
    new = ''
    for letter in text:
        if letter == ' ':
            index = text.index(letter)
            new += text[index]
    for letter in text:
        index = alphabet.index(letter) - shift
        if index < 25:
            new += alphabet[index]
        else:
            new_index = index - 26
            new += alphabet[new_index]
    print(f"The encoded text is {new}")

from logo import logo
should_end = False
while not should_end:
  print(logo)  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if direction == 'encode':
      encyrpt(text, shift)
  else:
      decrypt(text, shift)
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")




