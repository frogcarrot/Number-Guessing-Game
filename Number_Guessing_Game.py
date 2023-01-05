def game(mystery_number, game_round, player_choice, wins, losses, os):
	
	game_round += 1
	
	if int(player_choice) == mystery_number:
		print("\nCorrect!")
		wins += 1
		game_round += 1
		print("You got it on round: " + str(game_round) + "!")
		print("\nWins: " + str(wins))
		print("Losses: " + str(losses))
		y_or_no = input("\nPlay again? (Y/N): ")
		os.system('cls')
		
		if y_or_no == "Y":
			mystery_number = random.randint(1, 10)
			game_round = -1
			player_choice = input("Guess the number (1-10): ")
			game(mystery_number, game_round, player_choice, wins, losses, os)
			
		elif y_or_no == "N":
			print("Okay, bitch.")
			exit()
	
	if game_round == 2:
		losses += 1
		print("\nGAME OVER!!!")
		print("\nWins: " + str(wins))
		print("Losses: " + str(losses))
		y_or_no = input("\nPlay again? (Y/N): ")
		os.system('cls')
		
		if y_or_no == "Y":
			mystery_number = random.randint(1, 10)
			game_round = -1
			player_choice = input("Guess the number (1-10): ")
			game(mystery_number, game_round, player_choice, wins, losses, os)
			
		elif y_or_no == "N":
			print("Okay, bitch.")
			exit()
			
	if int(player_choice) > mystery_number:
		print("\nIncorrect! The mystery number is lower...")
		input("\nPress enter to continue...")
		os.system('cls')
		player_choice = input("Guess again: ")
		game(mystery_number, game_round, player_choice, wins, losses, os)
		
	if int(player_choice) < mystery_number:
		print("\nIncorrect! The mystery number is higher...")
		input("\nPress enter to continue...")
		os.system('cls')
		player_choice = input("Guess again: ")
		game(mystery_number, game_round, player_choice, wins, losses, os)
		
import random, os

mystery_number = random.randint(1, 10)
game_round = -1
wins = 0
losses = 0

player_choice = input("Guess the number (1-10): ")
game(mystery_number, game_round, player_choice, wins, losses, os)
