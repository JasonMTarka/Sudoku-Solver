import tkinter as tk

from sudoku_solver import Sudoku
from sudoku_constants import NAMES, LOCATIONS


class MainApplication:
    """Class which creates tkinter GUI for Sudoku Solver program."""

    def __init__(self, sudoku: Sudoku, root) -> None:
        """Define grid, generate initial sudoku, and create UI."""

        self.outer_grids: dict[str, Inner_Grid] = {}
        self.sudoku = sudoku
        self.root = root
        self.setup()

    def generate(self) -> None:
        """Set the GUI grid to match the values of the grid variable."""

        for name in NAMES:
            for inner_name in NAMES:
                loc1, loc2 = LOCATIONS[name][inner_name]
                self.outer_grids[name].cells[inner_name].delete(0, tk.END)
                self.outer_grids[name].cells[inner_name].insert(
                    0, self.sudoku.grid[loc1][loc2]
                )

    def setup(self) -> None:
        """Create GUI grid."""

        grid_locs = list(LOCATIONS["topleft"].values())

        for i, name in enumerate(NAMES):
            self.outer_grids[name] = Inner_Grid(self.root)
            row_val, col_val = grid_locs[i]
            self.outer_grids[name].grid(
                row=row_val, column=col_val, padx=5, pady=5
            )

        solve_button = HoverButton(
            self.root,
            text="Solve",
            padx=15,
            pady=3,
            borderwidth=3,
            command=self._solve_sudoku_button,
        )
        solve_button.configure(activebackground="#d4d4ff")
        solve_button.grid(row=3, column=2)

        DIFFICULTY_OPTIONS = [
            "Easy #1",
            "Easy #2",
            "Easy #3",
            "Medium #1",
            "Medium #2",
            "Hard #1",
            "Super Hard #1",
        ]
        difficulty_clicked = tk.StringVar()
        difficulty_clicked.set(DIFFICULTY_OPTIONS[0])
        difficulty_bar = tk.OptionMenu(
            self.root, difficulty_clicked, *DIFFICULTY_OPTIONS
        )
        difficulty_bar.configure(activebackground="#d4d4ff")
        difficulty_bar.grid(row=3, column=0)

        new_sudoku_button = HoverButton(
            self.root,
            text="Generate Sudoku",
            padx=15,
            pady=3,
            borderwidth=3,
            command=lambda: self._prep_new_sudoku_button(difficulty_clicked),
        )
        new_sudoku_button.configure(activebackground="#d4d4ff")
        new_sudoku_button.grid(row=3, column=1)

        self.generate()

    def _prep_new_sudoku_button(self, difficulty: tk.StringVar) -> None:
        """Load new sudoku after being called by button."""

        self.sudoku.load_new(difficulty.get())
        self.generate()

    def _solve_sudoku_button(self) -> None:
        """Solve sudoku after being called by button."""

        self.sudoku.solve()
        self.generate()


class Inner_Grid(tk.Frame):
    """Define a 9-value grid (1/9 of complete sudoku)."""

    def __init__(self, root, **kwargs) -> None:
        """Initialize parent tkinter Frame and call cell_generation method."""

        super().__init__()
        self.cell_generation()

    def cell_generation(self) -> None:
        """Create a dictionary (self.cells) and insert sudoku values."""

        self.cells = {}
        for name in NAMES:
            self.cells[name] = tk.Entry(self, width=4, borderwidth=2, font="8")
            for inner_name in NAMES:
                row_val, col_val = LOCATIONS[name][inner_name]
                self.cells[name].grid(row=row_val, column=col_val)


class HoverButton(tk.Button):
    """Allow button to change color when hovered over."""

    def __init__(self, root, **kwargs) -> None:
        """Initialize tkinter button and bind Enter and Leave actions."""

        tk.Button.__init__(self, master=root, **kwargs)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, z) -> None:
        """Define entrance action."""

        self["background"] = self["activebackground"]

    def on_leave(self, z) -> None:
        """Define exit action."""

        self["background"] = self.defaultBackground


def main() -> None:
    """Instantiate objects and launch tkinter GUI."""

    sudoku = Sudoku()
    root = tk.Tk()
    MainApplication(sudoku, root)
    root.title("Sudoku Solver")
    root.geometry("409x290")
    tk.mainloop()


if __name__ == "__main__":
    main()
