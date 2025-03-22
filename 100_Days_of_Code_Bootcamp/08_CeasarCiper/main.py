import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Encryption
#---------------------------------------------
def caesar(text_to_encrypt,shift_number,direction):

  encrypted_message = ""

  for r in range(0,len(text_to_encrypt)):      
    
    found = False

    for l in range(0,26):  
      if(alphabet[l] == text_to_encrypt[r]):

        found = True

        if(direction == "encrypt"):
          k = l+shift_number
          while k >= 26:
            k -= 26

        if(direction == "decrypt"):            
          k = l-shift_number
          while k < 0:
            k += 26
        encrypted_message += alphabet[k]
    if found == False:
      encrypted_message += text_to_encrypt[r]
      
  print(encrypted_message)
#---------------------------------------------

if(direction == "encode"):
  caesar(text,shift,"encrypt")

if(direction == "decode"):
  caesar(text,shift,"decrypt")