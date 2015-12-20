import random


def guessing_game():
	x = random.randint(1, 9)
	user_guess_count = 0
	print ("\nTo exit at any point, type exit\n")

	while True:	
		user_guess = input("What number am I thinking of between 1 & 9: ")
		
		if user_guess.isdigit():	
			if (int(user_guess) <= 0) or (int(user_guess) >= 10):
				print ("You must enter a number between 1 to 9 or exit to quit the game")
				continue
			else:	
				user_guess_count += 1
				if int(user_guess) > x:
					print ("Lower")
				elif int(user_guess) < x:
					print ("Higher")
				elif int(user_guess) == x:
					if user_guess_count == 1:
						print ("\nYou guessed it!\nIt took you " + str(user_guess_count) + " guess to get the right number\n")
					else:
						print ("\nYou guessed it!\nIt took you " + str(user_guess_count) + " guesses to get the right number\n")
						x = random.randint(1, 9)
						user_guess_count = 0
		
		elif user_guess.isalpha():
			if str(user_guess).lower() == "exit":
				print ("\nThank you for playing\n")
				break
			else:
				print ("You must enter a number between 1 to 9 or exit to quit the game")
				continue


if __name__ == "__main__":
	guessing_game()
