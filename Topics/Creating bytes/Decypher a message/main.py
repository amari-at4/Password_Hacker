ciphered_message = input()
key_number = (int(input())).to_bytes(2, byteorder='big')

real_key = key_number[0] + key_number[1]

deciphered_message = []

for character in ciphered_message:
    deciphered_message.append(chr(ord(character) + real_key))

print("".join(deciphered_message))
