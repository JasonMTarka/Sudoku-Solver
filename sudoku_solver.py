import copy

# Try block is for website use; except block is for execution as main file
try:
    from portfolio_site.sudoku.Sudoku_Solver.sudoku_constants import SUDOKUS, GRIDFINDER
except ModuleNotFoundError:
    from sudoku_constants import SUDOKUS, GRIDFINDER


class Sudoku:
    def __init__(self, difficulty: str = "Easy #1") -> None:
        self.grid = SUDOKUS.get(difficulty)
        self.difficulty = difficulty
        self._rows = {}
        for i in range(0, 9):
            self._rows[i] = self.grid[i]

    def __repr__(self) -> str:
        return f"{self.grid}"

    def load_new(self, difficulty: str) -> None:
        self.grid = SUDOKUS[difficulty]
        self.difficulty = difficulty

    def reset(self) -> None:
        self.grid = SUDOKUS[self.difficulty]

    def print_sudoku(self) -> None:
        for row in self.grid:
            print(row)

    def solve(self) -> None:
        self._recursive_solver()
        self.grid = self._saved_grid

    def _recursive_solver(self) -> None:
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

    def _valid_spot(self, guess: int, row: int, col: int) -> bool:
        def _row_check() -> bool:
            if guess in self.grid[row - 1]:
                return False
            else:
                return True

        def _col_check() -> bool:
            for j in range(0, 9):
                if guess == self.grid[j][col - 1]:
                    return False
                else:
                    pass
            return True

        def _grid_check() -> bool:
            def _inner_check(grid_num: int) -> bool:
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
        return False
