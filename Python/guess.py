#!/usr/bin/python
import random

number = random.randint(1, 50)
numGuesses = 0
maxGuesses = 5

while numGuesses < maxGuesses:
	try: 
		guess = int(input("Guess a number between 1 and 50: "))
		if (guess > 50) or (guess < 1):
			print("Enter a number between 1 and 50, dipshit")
			continue
	except ValueError:
		print("You must eneter an integer!")
		continue
	except:
		print("An unknown error as occured: ")
		continue

	numGuesses += 1

	if (guess == number): 
		print("You Win!")
		break
	if (numGuesses == maxGuesses):
		print("You Suck, Go Away")
	
