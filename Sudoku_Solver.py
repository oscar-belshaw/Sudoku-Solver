#Initialise the board to be solved here, 0 represents a blank space
board = [
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 1, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 2, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	
	]

def solve(bd):
	 
	 find = find_empty(bd)
	 if not find:
		 return True
	 else:
		 row, col = find
		 
	 for i in range(1, 10):
		 if valid(bd, i, (row, col)):
			 bd[row][col] = i 
			 
			 if solve(bd):
				 return True
				 
			 bd[row][col] = 0
			 
	 return False
				
			 
	
#This checks to see that an input is valid
#ie the input number isn't already in a conflicting row, column or square
def valid(bd, num, pos):
	
	#check row
	for i in range(len(bd[0])):
		if bd[pos[0]][i] == num and pos[1] != i:
			return False
	#check column
	for i in range(len(bd)):
		if bd[i][pos[1]] == num and pos[0] != i:
			return False
	#check square
	box_x = pos[1] // 3
	box_y = pos[0] // 3
	
	for i in range(box_y * 3, box_y*3 + 3):
		for j in range(box_x * 3, box_x*3 + 3):
			if bd[i][j] == num and (i, j) != pos:
				return False
	return True


def print_board(bd):
	for i in range(len(bd)):
		if i % 3 == 0 and i != 0:
			print("- - - - - - - - - - - ") #Prints a horizontal line after ever 3 rows
			
		for j in range(len(bd[0])):
			if j % 3 == 0 and j != 0:
				print("| ", end="") #Prints a vertical line after every 3 columns
				
			if j == 8:
				print(bd[i][j])
			else: 
				print(str(bd[i][j]) + " ", end="")
			
#Checks for empty tiles, represented by a 0
def find_empty(bd):
	for i in range(len(bd)):
		for j in range(len(bd[0])):
			if bd[i][j] == 0:
				return (i, j) #returns the row followed by column (ie (y,x) instead of (x, y)
	return None
				

print_board(board)
solve(board)
print( "__________________________\n") #This just creates a divisor between the two boards
print_board(board)
