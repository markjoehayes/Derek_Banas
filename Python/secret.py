#!/usr/bin/python3

# Enter a string to hide in uppercase
# convert to unicode (secret message)
# print original message

secret_string = ""
translated_string = ""
message = input("Enter a string in uppercase letters: ")
for char in message:
	secret_string += str(ord(char))
print(secret_string)
for i in range(0, len(secret_string) -1, 2):
	char_code = secret_string[i] + secret_string[i + 1]

	

