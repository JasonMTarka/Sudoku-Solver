import tkinter as tk
import copy

try:
    from portfolio_site.sudoku.Sudoku_Solver.sudoku_constants import NAMES, LOCATIONS, SUDOKUS, GRIDFINDER
except ModuleNotFoundError:
    from sudoku_constants import NAMES, LOCATIONS, SUDOKUS, GRIDFINDER


class MainApplication:
    def __init__(self, sudoku, root):
        self.outer_grids = {}
        self.sudoku = sudoku
        self.root = root
        self.setup()

    def generate(self):
        # Sets the GUI grid to match the values of the grid variable
        for inner_grid in self.outer_grids:
            for name in NAMES:
                for inner_name in NAMES:
                    loc1, loc2 = LOCATIONS[name][inner_name]
                    self.outer_grids[name].cells[inner_name].delete(0, tk.END)
                    self.outer_grids[name].cells[inner_name].insert(0, self.sudoku.grid[loc1][loc2])

    def setup(self):
        grid_locs = list(LOCATIONS["topleft"].values())

        for i, name in enumerate(NAMES):
            self.outer_grids[name] = Inner_Grid(self.root)
            row_val, col_val = grid_locs[i]
            self.outer_grids[name].grid(row=row_val, column=col_val, padx=5, pady=5)

        solve_button = HoverButton(self.root, text="Solve", padx=15, pady=3, borderwidth=3, command=self._solve_sudoku_button)
        solve_button.configure(activebackground="#d4d4ff")
        solve_button.grid(row=3, column=2)

        DIFFICULTY_OPTIONS = ["Easy #1", "Easy #2", "Easy #3", "Medium #1", "Medium #2", "Hard #1", "Super Hard #1"]
        difficulty_clicked = tk.StringVar()
        difficulty_clicked.set(DIFFICULTY_OPTIONS[0])
        difficulty_bar = tk.OptionMenu(self.root, difficulty_clicked, *DIFFICULTY_OPTIONS)
        difficulty_bar.configure(activebackground="#d4d4ff")
        difficulty_bar.grid(row=3, column=0)

        new_sudoku_button = HoverButton(self.root, text="Generate Sudoku", padx=15, pady=3, borderwidth=3, command=lambda: self._prep_new_sudoku_button(difficulty_clicked))
        new_sudoku_button.configure(activebackground="#d4d4ff")
        new_sudoku_button.grid(row=3, column=1)

        self.generate()

    def _prep_new_sudoku_button(self, difficulty):
        self.sudoku.load_new(difficulty.get())
        self.generate()

    def _solve_sudoku_button(self):
        self.sudoku.solve()
        self.generate()


class Sudoku:
    def __init__(self, difficulty="Easy #1"):
        self.grid = SUDOKUS.get(difficulty)
        self.difficulty = difficulty
        self._rows = {}
        for i in range(0, 9):
            self._rows[i] = self.grid[i]

    def __repr__(self):
        return f"{self.grid}"

    def load_new(self, difficulty):
        self.grid = SUDOKUS[difficulty]
        self.difficulty = difficulty

    def reset(self):
        self.grid = SUDOKUS[self.difficulty]

    def print_sudoku(self):
        for row in self.grid:
            print(row)

    def solve(self):
        self._recursive_solver()
        self.grid = self._saved_grid

    def _recursive_solver(self):
        for x in range(1, 10):
            for y in range(1, 10):
                if self.grid[x - 1][y - 1] == 0:
                    for i in range(1, 10):
                        if self._valid_spot(i, x, y):
                            self.grid[x - 1][y - 1] = i
                            self._recursive_solver()
                            self.grid[x - 1][y - 1] = 0
                    return
                else:
                    pass
        self._saved_grid = copy.deepcopy(self.grid)

    def _valid_spot(self, guess, row, col):
        def _row_check():
            if guess in self.grid[row - 1]:
                return False
            else:
                return True

        def _col_check():
            for j in range(0, 9):
                if guess == self.grid[j][col - 1]:
                    return False
                else:
                    pass
            return True

        def _grid_check():
            def _inner_check(grid_num):
                section_bot_and_top = GRIDFINDER[grid_num]
                section_bot, section_top, bot, top = section_bot_and_top
                for i in range(section_bot, section_top):
                    if guess in self.grid[i][bot:top]:
                        return False
                    else:
                        pass
                return True

            if row <= 3:
                if col <= 3:
                    return _inner_check(1)
                elif col >= 4 and col < 7:
                    return _inner_check(2)
                else:
                    return _inner_check(3)

            elif row >= 4 and row < 7:
                if col <= 3:
                    return _inner_check(4)
                elif col >= 4 and col < 7:
                    return _inner_check(5)
                else:
                    return _inner_check(6)

            else:
                if col <= 3:
                    return _inner_check(7)
                elif col >= 4 and col < 7:
                    return _inner_check(8)
                else:
                    return _inner_check(9)

        if _row_check():
            if _col_check():
                if _grid_check():
                    return True
        else:
            pass

# Inner grid refers to a 9-cell grid


class Inner_Grid(tk.Frame):
    def __init__(self, root, **kwargs):
        super().__init__()
        self.cell_generation()

    def cell_generation(self):
        self.cells = {}
        for name in NAMES:
            self.cells[name] = tk.Entry(self, width=4, borderwidth=2, font=8)
            for inner_name in NAMES:
                row_val, col_val = LOCATIONS[name][inner_name]
                self.cells[name].grid(row=row_val, column=col_val)

# Allows button to change color when hovered over


class HoverButton(tk.Button):
    def __init__(self, root, **kwargs):
        tk.Button.__init__(self, master=root, **kwargs)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, z):
        self["background"] = self["activebackground"]

    def on_leave(self, z):
        self["background"] = self.defaultBackground


def main():
    sudoku = Sudoku()
    root = tk.Tk()
    MainApplication(sudoku, root)
    root.title("Sudoku Solver")
    root.geometry("409x290")
    tk.mainloop()


if __name__ == "__main__":
    main()
