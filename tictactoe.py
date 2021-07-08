import random
import copy

board  = [['-','-','-'],['-','-','-'],['-','-','-']]

'''
- - - 
- - -
- - - 
'''
name1 = ""
name2 = ""
gametype = ""
player1 = ["", ""]
player2 = ["", ""]

def game():
	global gametype
	if gametype == "":
		gametype = input("Do you want to play against the computer (Y/N)")
	counter = 0
	global name1
	global name2
	if name1 == "":
		name1 = input("Enter player 1's name: ")
	player1[0] = name1
	if gametype.upper() == "N" and name2 == "":
		name2 = input("Enter player 2's name: ")
	player2[0] = name2
	if gametype.upper() == "Y":
		player2[0] = "Computer"
	player1[1], player2[1] = random_move()
	print(player1[0] + " is " + player1[1])
	print(player2[0] + " is " + player2[1])
	current_player = choose_random_player()
	print(current_player[0] + " starts!")
	print_board()
	while True:
		if current_player[0] != "Computer":
			move = int(input(current_player[0] + " choose a number between 0 and 8: "))
			while not possible(move):
				move = int(input("Illegal Move. Choose another number between 0 and 8: "))
		else:
			move = computer_move(current_player[1])
			print("Computer plays move: ", move)
		make_move(board, current_player[1], move)
		counter += 1
		if is_winner(board, current_player[1]):
			print_board()
			print("Winner:", current_player[0])
			reset_board()
			break
		print_board()
		if counter == 9:
			print("The Game ended in a Tie!")
			reset_board()
			break
		current_player = other(current_player)



def choose_random_player():
	x = random.randint(0, 1)
	if x == 0:
		return player1
	else:
		return player2

def random_move():
	x = random.randint(0, 1)
	if x == 0:
		return "X", "O"
	else:
		return "O", "X"


def other(player):
	if player == player1:
		return player2
	else:
		return player1

def make_move(b, piece, position):
	#piece = X or piece = O
	row = position // 3
	col = position % 3
	b[row][col] = piece

def print_board():
	for row in board:
		for element in row:
			print(element + " ", end="")
		print()

def is_winner(board, piece):
	if board[0][0] == piece and board[0][1] == piece and board[0][2] == piece:
		return True
	if board[1][0] == piece and board[1][1] == piece and board[1][2] == piece:
		return True
	if board[2][0] == piece and board[2][1] == piece and board[2][2] == piece:
		return True
	if board[0][0] == piece and board[1][0] == piece and board[2][0] == piece:
		return True
	if board[0][1] == piece and board[1][1] == piece and board[2][1] == piece:
		return True
	if board[0][2] == piece and board[1][2] == piece and board[2][2] == piece:
		return True
	if board[0][0] == piece and board[1][1] == piece and board[2][2] == piece:
		return True
	if board[0][2] == piece and board[1][1] == piece and board[2][0] == piece:
		return True
	return False

def possible(m):
	#make move? return True
	#cant make move? return False
	if type(m) != int:
		return False
	if m > 8 or m < 0:
		return False
	row, col = m // 3,  m % 3
	if board[row][col] == '-':
		return True
	else:
		return False

def reset_board():
	for i in range(len(board)):
		for j in range(len(board[i])):
			board[i][j] = '-'


def duplicate_board(b):
	test_list = copy.deepcopy(b)
	return test_list

def choose_random_move(bo, moves): 
	possible_moves = []
	for m in moves:
		if possible(m):
			possible_moves.append(m)

	if possible_moves:
		return random.choice(possible_moves)
	else:
		return None

def computer_move(c_piece):
	if c_piece == "X":     
		player_piece = "O"
	else:
		player_piece = "X"

	#CHECK IF COMPUTER CAN WIN IN THE NEXT MOVE
	#RETURN MOVE
	for i in range(0,9):
		copyboard = duplicate_board(board)
		if possible(i):
			make_move(copyboard, c_piece, i)
			if is_winner(copyboard, c_piece):
				return i

	#CHECK IF PLAYER CAN WIN STOP HIM
	for i in range(0,9):
		copyboard = duplicate_board(board)
		if possible(i):
			make_move(copyboard, player_piece, i)
			if is_winner(copyboard, player_piece):
				return i


	#CORNER PIECE
	m = choose_random_move(board, [0,2,6,8])
	if m != None:
		return m

	#CENTER PIECE
	if possible(4):
		return 4

	#SIDES
	m = choose_random_move(board, [1,3,5,7])
	if m != None:
		return m


if __name__ == "__main__":
	print("Welcome to tic tac toe")
	start = input ("Do you want to play? (Y/N)")
	start = start.upper()
	while start == "Y":
		game()
		start = input("Do you want to restart? (Y/N)")
	print("The END")
 


