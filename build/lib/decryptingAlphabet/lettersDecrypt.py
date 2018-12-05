#!/bin/python3

"""creating an alphabet variable for all alphabet
and an open message object"""
alphabet = 'abcdefghijklmnopqrstuvwxyz'
newMessage = ''

"""user message input"""
message = input('Please enter your crypted  message: ')

"""Choose a Ceasar's key (from 1-26)"""
key = input('Enter a key (1-26): ')
key = int(key)

"""Set the key in message to decrypt"""
for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    newPosition = (position - key) % 26
    newCharacter = alphabet[newPosition]
    newMessage += newCharacter
  else:
    newMessage += character

print('Your decrypted message is: ', newMessage)

