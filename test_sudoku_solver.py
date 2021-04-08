import unittest
import sudoku_solver

class TestSolver(unittest.TestCase):

    def setUp(self):
        self.sudoku = sudoku_solver.Sudoku(difficulty="Easy #1")

    def tearDown(self):
        pass

    def test_sudoku_initialize(self):
        self.assertEqual(type(self.sudoku.grid), type([]))
        self.assertEqual(len(self.sudoku.grid), 9)

    def test_sudoku_solve(self):
        sudoku = sudoku_solver.Sudoku(difficulty="Easy #1")
        sudoku.solve()
        self.assertEqual(sudoku.grid, [[1, 7, 3, 9, 5, 4, 6, 8, 2],
                                       [9, 5, 2, 6, 8, 1, 3, 7, 4],
                                       [8, 6, 4, 2, 7, 3, 9, 1, 5],
                                       [3, 1, 5, 7, 4, 9, 8, 2, 6],
                                       [4, 9, 8, 3, 2, 6, 7, 5, 1],
                                       [6, 2, 7, 5, 1, 8, 4, 9, 3],
                                       [7, 8, 6, 1, 3, 5, 2, 4, 9],
                                       [5, 4, 9, 8, 6, 2, 1, 3, 7],
                                       [2, 3, 1, 4, 9, 7, 5, 6, 8]])

        sudoku = sudoku_solver.Sudoku(difficulty="Medium #1")
        sudoku.solve()
        self.assertEqual(sudoku.grid, [[4, 7, 3, 1, 9, 5, 2, 6, 8],
                                       [8, 5, 6, 3, 4, 2, 7, 9, 1],
                                       [9, 2, 1, 6, 8, 7, 5, 3, 4],
                                       [3, 4, 7, 5, 2, 6, 1, 8, 9],
                                       [5, 8, 2, 9, 1, 4, 6, 7, 3],
                                       [6, 1, 9, 8, 7, 3, 4, 5, 2],
                                       [2, 3, 4, 7, 6, 9, 8, 1, 5],
                                       [1, 6, 5, 2, 3, 8, 9, 4, 7],
                                       [7, 9, 8, 4, 5, 1, 3, 2, 6]])

        sudoku = sudoku_solver.Sudoku(difficulty="Hard #1")
        sudoku.solve()
        self.assertEqual(sudoku.grid, [[6, 2, 9, 1, 8, 7, 5, 3, 4],
                                       [1, 8, 3, 5, 4, 2, 7, 9, 6],
                                       [5, 4, 7, 3, 9, 6, 2, 1, 8],
                                       [2, 5, 6, 9, 3, 1, 4, 8, 7],
                                       [4, 9, 8, 6, 7, 5, 3, 2, 1],
                                       [7, 3, 1, 8, 2, 4, 6, 5, 9],
                                       [8, 6, 2, 4, 1, 3, 9, 7, 5],
                                       [9, 7, 5, 2, 6, 8, 1, 4, 3],
                                       [3, 1, 4, 7, 5, 9, 8, 6, 2]])

    def test_load_new(self):
        sudoku = sudoku_solver.Sudoku()
        sudoku.load_new(difficulty="Medium #2")
        self.assertEqual(sudoku.grid, [[0, 0, 0, 4, 8, 0, 2, 0, 9],
                                       [0, 0, 0, 0, 7, 0, 0, 5, 1],
                                       [0, 8, 3, 0, 2, 0, 0, 0, 0],
                                       [0, 0, 4, 0, 0, 0, 0, 0, 0],
                                       [7, 6, 0, 0, 0, 0, 0, 0, 2],
                                       [0, 5, 0, 7, 0, 9, 0, 0, 0],
                                       [0, 0, 7, 0, 0, 5, 9, 0, 4],
                                       [0, 0, 0, 0, 0, 0, 5, 0, 0],
                                       [4, 0, 0, 8, 0, 0, 6, 7, 0]])

    def test_reset(self):
        sudoku = sudoku_solver.Sudoku()
        sudoku.solve()
        sudoku.reset()
        self.assertEqual(sudoku.grid, [[1, 0, 0, 9, 0, 4, 0, 8, 2],
                                       [0, 5, 2, 6, 8, 0, 3, 0, 0],
                                       [8, 6, 4, 2, 0, 0, 9, 1, 0],
                                       [0, 1, 0, 0, 4, 9, 8, 0, 6],
                                       [4, 9, 8, 3, 0, 0, 7, 0, 1],
                                       [6, 0, 7, 0, 1, 0, 0, 9, 3],
                                       [0, 8, 6, 0, 3, 5, 2, 0, 9],
                                       [5, 0, 9, 0, 0, 2, 1, 3, 0],
                                       [0, 3, 0, 4, 9, 7, 0, 0, 8]],)


if __name__ == "__main__":
    unittest.main()
