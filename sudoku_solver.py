
grid = [
		[1,0,0,9,0,4,0,8,2],
		[0,5,2,6,8,0,3,0,0],
		[8,6,4,2,0,0,9,1,0],
		[0,1,0,0,4,9,8,0,6],
		[4,9,8,3,0,0,7,0,1],
		[6,0,7,0,1,0,0,9,3],
		[0,8,6,0,3,5,2,0,9],
		[5,0,9,0,0,2,1,3,0],
		[0,3,0,4,9,7,0,0,8]
		]

def checker(guess,row,col):

	def row_check():
		if guess in grid[row-1]:
			return False
		else:
			return True

	def col_check():
		for j in range(0,9):
			if guess == grid[j][col-1]:
				return False
			else:
				pass
		return True

	def grid_checker():

		def inner_check(grid_num):
			
			"""
			9-square grids are defined by the following dictionary, with grids 1-3 being the top, 
			grids 4-6 being the middle, and grids 7-9 being the bottom of the entire puzzle
			"""
			gridfinder = {
			1: (0,3,0,3),
			2: (0,3,3,6),
			3: (0,3,6,9),
			4: (3,6,0,3),
			5: (3,6,3,6),
			6: (3,6,6,9),
			7: (6,9,0,3),
			8: (6,9,3,6),
			9: (6,9,6,9)
			}

			section_bot_and_top = gridfinder[grid_num]

			"""
			Sections refer to 3-row groups (grids 1-3, grids 4,6, 
			and grids 7-9 make up the three sections
			""" 
			section_bot, section_top, bot, top = section_bot_and_top
			for i in range(section_bot, section_top):
					if guess in grid[i][bot:top]:
						return False
					else:
						pass
			return True

		if row <= 3:
			if col <= 3:
				if inner_check(1):
					return True
			elif col >= 4 and col < 7:
				if inner_check(2):
					return True
			else:
				if inner_check(3):
					return True

		elif row >= 4 and row < 7:
			if col <= 3:
				if inner_check(4):
					return True
			elif col >= 4 and col < 7:
				if inner_check(5):
					return True
			else:
				if inner_check(6):
					return True

		else:
			if col <= 3:
				if inner_check(7):
					return True

			elif col >= 4 and col < 7:
				if inner_check(8):
					return True
			else:
				if inner_check(9):
					return True

	if row_check():
		if col_check():
			if grid_checker():
				return True
		else:
			pass

# Primary solver function which uses recursion and backtracking to find the solution
def solver():
	for x in range(1,10):
		for y in range(1,10):
			if grid[x-1][y-1] == 0:
				for i in range(1,10):
					if checker(i,x,y):
						grid[x-1][y-1] = i
						solver()
						grid[x-1][y-1] = 0
					
				return

			else:
				pass

	for i in range(9):
		print(grid[i])
	
solver()
