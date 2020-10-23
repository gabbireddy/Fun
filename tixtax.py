#The aim of this software program is to create an interactive Tic Tac Toe game between two players.

#Algorithm to create an interactice Tic Tac Toe game:
#		1) Create a Tic Tac Toe board.
#		2) Give player_1 the choice to choose between X and O
#		3) Assign the choosen symbol to player_1 and the left over symbol to player_2
#
#
#		#Start While Loop
#		4) Ask player_1 which index position does he want to mark his symbol. (Update list)
#		5) Check for "Victory":
#						if Victory == True:
#								Declare Player 1 as winner and exit the loop
#						else:
#							Ask player_2 the index position and update list
#							Check for "Victory"
#							if Victory == True:
#								Declare Player 2 as winner and exit the loop
#							else:
#								Go back to step 4
#
# 		#Victory:
#			#  Create 8 win conditions
#			#  Check if any 1 of the 8 conditions is True
#			#  If True, then assign True to Victory



#TO DO NEXT
# Validate user input while assigning X or O
# Validate user input while giving the index position
# Create an instance for Draw
# Ask the user if he wants to play again
# Validate the index input such that a player cannot overwrite a symbol in a game
# Validate user input for playing again! 

print("RULES OF THE GAME:\n")
print("This is a game played between two players\n \nOne player chooses X and the other one gets an O \n")
print("You will be playing the game on a 3x3 board\n \nThe first player to get 3 X's or O's in a line wins the game\n")
print("Each box is labelled from 1 to 9, press the number of the box to mark your symbol")
print("\nThe first box in the first row is 1, the second box in first row is 2 and so on...\n")
input("Okay, so let's start the game \n  \nPress ENTER to continue")
def tixtax():

	#BOARD
	b = ["#","","","","","","","","",""]

	def display_board():
		print('\n'*100)
		print(f"  {b[1]} | {b[2]} | {b[3]}")
		print("  ----------")
		print(f"  {b[4]} | {b[5]} | {b[6]}")
		print("  ----------")
		print(f"  {b[7]} | {b[8]} | {b[9]}")

#ASSIGN X or O to player 1
	players = {"player_1":"temp","player_2":"temp"}



	def assign_marker():
	
		holder = False

		while holder == False: #For validating the user input


			players["player_1"] = input("Player 1, choose a symbol between X and O \n").upper() #Assigning player_1 symbol

			if players["player_1"] in ('X','O'):
				holder = True
			else:
				print("Please choose a symbol between X and O only \n")


		if players["player_1"] == "X": #Assigning player_2 symbol
			players["player_2"] = "O"
		else:
			players["player_2"] = "X"

	assign_marker()


#Victory Checker
	def check_victory():

		if ((b[1] == b[2]) and (b[1] == b[3])) and b[1] != "":
			return True
		elif ((b[4] == b[5]) and (b[5] == b[6])) and b[4] != "":
			return True
		elif ((b[7] == b[8]) and (b[8] == b[9])) and b[7] != "":
			return True
		elif ((b[1] == b[4]) and (b[4] == b[7])) and b[1] != "":
			return True
		elif ((b[2] == b[5]) and (b[5] == b[8])) and b[2] != "":
			return True
		elif ((b[3] == b[6]) and (b[6] == b[9])) and b[3] != "":
			return True
		elif ((b[9] == b[5]) and (b[5] == b[1])) and b[1] != "":
			return True
		elif ((b[3] == b[5]) and (b[5] == b[7])) and b[3] != "":
			return True
		else:
			pass
#WHILE LOOP

	whilelooper = False

	while whilelooper == False:


		print("\n")

	#validating user input
		jason = False

		while jason == False:
			n = input("Player 1, enter the position at which you wanna mark \n")
			if n in ['1','2','3','4','5','6','7','8','9']:
				n = int(n)
				if b[n] == "":
					jason = True
				else:
					print("\n You cannot overwrite an existing symbol \n")
				
				
			else:
				print("\n")
				print("Please choose an index value between 1 and 9 \n")


		b[n] = players["player_1"] #List updated


		print("\n")
		display_board()


		xanax = check_victory()
		if xanax == True:
					print("\n")
					print("Player 1 is winner")

					play_again = input("Do you wanna play again (Y/N)? \n")
					if play_again in ['y','Y']:
						tixtax()
					if play_again in ['n','N']:
						print("\nThanks for playing, bye")
						break

		elif "" not in b:
			print("\n")
			print("DRAW GAME \n")
			play_again = input("Do you wanna play again (Y/N)? \n")
			if play_again in ['y','Y']:
				tixtax()
			if play_again in ['n','N']:
				print("\nThanks for playing, bye")
				break

			


		else:

		

			print("\n")
			while jason == True:

				n = input("Player 2, enter the position at which you wanna mark \n")
				if n in ['1','2','3','4','5','6','7','8','9']:
					n = int(n)
					if b[n] == "":
						jason = False
					else:
						print("\n You cannot overwrite an existing symbol \n")
				else:
					print("\n")
					print("Please choose an index value between 1 and 9 \n")


			b[n] = players["player_2"]


			print("\n")
			display_board()


			xanax = check_victory()
			if xanax == True:
				print("\n")			
				print("Player 2 is winner")
				break
			else:
				pass

tixtax()
