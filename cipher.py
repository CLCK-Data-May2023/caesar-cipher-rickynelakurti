# add your code here

sentence = input("Please enter a sentence: ")
sentence = sentence.lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
shifted_alphabet = 'fghijklmnopqrstuvwxyzabcde'

encrypted_sentence = ''

for char in sentence:
    if char in alphabet:
        index = alphabet.index(char)
        encrypted_sentence += shifted_alphabet[index]
    else:
        encrypted_sentence += char
print("The encrypted sentence is:", encrypted_sentence)