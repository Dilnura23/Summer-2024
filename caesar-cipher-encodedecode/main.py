alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
   
def caesar(user_text, amount_shift, cipher_direction):
    new_user_text = ""
    if cipher_direction == 'decode':
        amount_shift*= -1
    for x in user_text:
        if x!= " ":
            position_current = alphabet.index(x)
            if (len(alphabet)-1) - position_current >= amount_shift:
                x = alphabet[position_current+amount_shift] 
                new_user_text+=x
            else:
                x = alphabet[shift-1 - (len(alphabet)-1) + position_current ]
                new_user_text+=x
        else:
            new_user_text+=x
    print(f'The {cipher_direction} text is {new_user_text}')
    
caesar(text, shift, direction)

