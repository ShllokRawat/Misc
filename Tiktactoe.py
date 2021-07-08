board=[['-','-','-'], ['-','-','-'], ['-','-','-']]
def make_move(piece, position):
	row = position // 3
	col = position % 3
	board[row][col] = piece

def print_board():
	for row in board:
		for element in row:
			print(element + "", end="")

def is_winner(piece):
	if board[0][0] == piece and board[0][1] == piece and board[0][2] == piece:
		return True
	elif board[1][0] == piece and board[1][1] == piece and board[1][2] == piece:
		return True
	elif board[3][0] == piece and board[3][1] == piece and board[3][2] == piece:
		return True
	elif board[0][0] == piece and board[0][0] == piece and board[0][0] == piece:
		return True
	elif board[0][1] == piece and board[0][1] == piece and board[0][1] == piece:
		return True
	elif board[0][2] == piece and board[0][2] == piece and board[0][2] == piece:
		return True
	elif board[0][0] == piece and board[1][1] == piece and board[2][2] == piece:
		return True
	elif board[2][2] == piece and board[1][1] == piece and board[0][0] == piece:
		return True
	else:
		return False