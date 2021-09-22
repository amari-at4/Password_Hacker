text_to_cipher = input()
ciphered_text = []
for character in text_to_cipher:
    ciphered_text.append(chr(ord(character) + 1))

print("".join(ciphered_text))
