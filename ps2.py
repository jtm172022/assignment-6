###### this is the second .py file ###########

####### write your code here ##########

def tic_tac_toe():
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
end = False
win_commbinations = (sum=15)

# our output look

def draw() :
print( '\n -----')
print( '|' + board[0] + '|' + board[1] + '|' + board[2] + '|')
print( ' -----')
print( '|' + board[3] + '|' + board[4] + '|' + board[5] + '|')
print( ' -----')
print( '|' + board[6] + '|' + board[7] + '|' + board[8] + '|')
print( ' -----\n')

def p1():
        	print( "Player 1’s chance")
		for i in range(0,2)
			Position = int(raw_input("Enter position"))
			Number = int(raw_input("Enter Number"))

		if (Number==1 or Number ==3 or Number == 5 or Number == 7 or Number == 9):
			Board[Position]=Number
			printBoard() # Printing Board if valid move
			if(int(Board[0])+int(Board[1])+int(Board[2]) =15 or (int(Board[3])+int(Board[4])+int(Board[5]) =15 or (int(Board[6])+int(Board[7])+int(Board[8]) =15 or int(Board[0])+int(Board[3])+int(Board[7]) =15 or (int(Board[1])+int(Board[4])+int(Board[7]) =15 or (int(Board[2])+int(Board[5])+int(Board[8]) =15 or int(Board[0])+int(Board[4])+int(Board[8]) =15 or (int(Board[2])+int(Board[4])+int(Board[6]) =15):
				print("Player 1 wins)
			
		else :
			print("Invalid")
			continue 

def p2():
        	print( "Player 2’s chance")
		for i in range(0,2)
			Position = int(raw_input("Enter position"))
			Number = int(raw_input("Enter Number"))

		if (Number==2 or Number ==4 or Number == 6 or Number == 8):
			Board[Position]=Number
			printBoard() # Printing Board if valid move
			if(int(Board[0])+int(Board[1])+int(Board[2]) =15 or (int(Board[3])+int(Board[4])+int(Board[5]) =15 or (int(Board[6])+int(Board[7])+int(Board[8]) =15 or int(Board[0])+int(Board[3])+int(Board[7]) =15 or (int(Board[1])+int(Board[4])+int(Board[7]) =15 or (int(Board[2])+int(Board[5])+int(Board[8]) =15 or int(Board[0])+int(Board[4])+int(Board[8]) =15 or (int(Board[2])+int(Board[4])+int(Board[6]) =15):
				print("Player 2 wins)
			
		else :
			print("Invalid")
			continue 


