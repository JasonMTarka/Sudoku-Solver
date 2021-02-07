import tkinter as tk
from sudoku_constants import NAMES, LOCATIONS, SUDOKUS

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

# Inner grid refers to a 9-cell grid
class Inner_Grid(tk.Frame):
	
	def __init__(self, root, **kwargs):
		super().__init__()
		self.cell_generation()

	def cell_generation(self):

		self.cells = {}
		for name in NAMES:
			self.cells[name] = tk.Entry(self, width=4, borderwidth=2,font=8)
			for inner_name in NAMES:
				row_val, col_val = LOCATIONS[name][inner_name]
				self.cells[name].grid(row=row_val, column=col_val)

# Allows button to change color when hovered over
class HoverButton(tk.Button):

	def __init__(self, master, **kwargs):
		tk.Button.__init__(self,master=master,**kwargs)
		self.defaultBackground=self["background"]
		self.bind("<Enter>", self.on_enter)
		self.bind("<Leave>", self.on_leave)

	def on_enter(self,z):
		self["background"] = self["activebackground"]

	def on_leave(self,z):
		self["background"] = self.defaultBackground

def main():
	global root
	root = tk.Tk()
	root.title("Sudoku Solver")
	root.geometry("409x290")
	setup()
	tk.mainloop()

# Defines and sets up GUI
def setup():
	global outer_grids
	outer_grids = {}
	grid_locs = list(LOCATIONS["topleft"].values())

	for i, name in enumerate(NAMES):
		outer_grids[name] = Inner_Grid(root)
		row_val, col_val = grid_locs[i]
		outer_grids[name].grid(row=row_val, column=col_val, padx=5, pady=5)

	solve_button = HoverButton(root,text="Solve", padx=15, pady=3,borderwidth=3,command=solver)
	solve_button.configure(activebackground="#d4d4ff")
	solve_button.grid(row=3,column=2)
	
	DIFFICULTY_OPTIONS = ["Easy #1","Easy #2","Easy #3","Medium #1","Medium #2","Hard #1","Super Hard #1"]
	difficulty_clicked = tk.StringVar()
	difficulty_clicked.set(DIFFICULTY_OPTIONS[0])
	difficulty_bar = tk.OptionMenu(root,difficulty_clicked,*DIFFICULTY_OPTIONS)
	difficulty_bar.configure(activebackground="#d4d4ff")
	difficulty_bar.grid(row=3,column=0)
	
	new_sudoku_button = HoverButton(root, text="Generate Sudoku", padx=15, pady=3, borderwidth=3,command= lambda: make_new_sudoku(difficulty_clicked))
	new_sudoku_button.configure(activebackground="#d4d4ff")
	new_sudoku_button.grid(row=3,column=1)

	generate(grid)

# Sets the GUI grid to match the values of the grid variable
def generate(grid):
	for inner_grid in outer_grids:
		for name in NAMES:
			for inner_name in NAMES:
				loc1,loc2 = LOCATIONS[name][inner_name]
				outer_grids[name].cells[inner_name].delete(0,tk.END)
				outer_grids[name].cells[inner_name].insert(0,grid[loc1][loc2])

# Sets the grid variable to a new sudoku grid contained within the sudoku_constants file
def make_new_sudoku(difficulty):
	global grid 
	grid = SUDOKUS[difficulty.get()]
	return generate(grid)

# Primary checker function which checks if a guess value is alreadylocated in the row, column, and inner grid 
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

	generate(grid)
	print()

if __name__ == "__main__":
	main()
