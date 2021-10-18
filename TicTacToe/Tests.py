import unittest
from main import TicTacToe


class EmptyConstructor(unittest.TestCase):
    def setUp(self):
        self.data = TicTacToe()

    def test_result(self):
        ttt = self.data
        self.assertEqual(ttt.size, 3)
        self.assertEqual(ttt.player1, "player1")
        self.assertEqual(ttt.player2, "player2")


class ConstructorWithStrings(unittest.TestCase):

    def test_result(self):
        self.assertRaises(UserWarning, TicTacToe, 5, "some string", "some string")


class CheckWinLine1(unittest.TestCase):
    def setUp(self):
        self.data = TicTacToe()
        self.data.array = ["X", "X", "X", "1", "2", "3", "4", "5", "7"]

    def test_result(self):
        ttt = self.data
        self.assertTrue(ttt.check_win(3))


class CheckWinLine2(unittest.TestCase):
    def setUp(self):
        self.data = TicTacToe()
        self.data.array = ["1", "2", "3", "1", "2", "3", "O", "O", "O"]

    def test_result(self):
        ttt = self.data
        self.assertTrue(ttt.check_win(7))


class CheckWinLine3(unittest.TestCase):
    def setUp(self):
        self.data = TicTacToe()
        self.data.array = ["a", "s", "s", "1", "2", "3", "O", "X", "O"]

    def test_result(self):
        ttt = self.data
        self.assertFalse(ttt.check_win(5))


class CheckWinLine4(unittest.TestCase):
    def setUp(self):
        self.data = TicTacToe()
        self.data.array = ["1", "2", "3", "R", "R", "R",  "4", "5", "7"]

    def test_result(self):
        ttt = self.data
        self.assertTrue(ttt.check_win(5))


class CheckWinCol(unittest.TestCase):
    def setUp(self):
        self.data = TicTacToe()
        self.data.array = ["X", "2", "3", "X", "4", "5", "X", "6", "7"]

    def test_result(self):
        ttt = self.data
        self.assertTrue(ttt.check_win(7))


class CheckWinCol1(unittest.TestCase):
    def setUp(self):
        self.data = TicTacToe()
        self.data.array = ["1", "O", "X", "2", "O", "3", "4", "O", "7"]

    def test_result(self):
        ttt = self.data
        self.assertTrue(ttt.check_win(5))


class CheckWinCol2(unittest.TestCase):
    def setUp(self):
        self.data = TicTacToe()
        self.data.array = ["1", "2", "X", "3", "4", "X", "5", "6", "O"]

    def test_result(self):
        ttt = self.data
        self.assertFalse(ttt.check_win(9))


class CheckWinCol3(unittest.TestCase):
    def setUp(self):
        self.data = TicTacToe()
        self.data.array = ["1", "O", "2", "3", "O", "4", "5", "O", "6"]

    def test_result(self):
        ttt = self.data
        self.assertTrue(ttt.check_win(5))


class CheckWinCol4(unittest.TestCase):
    def setUp(self):
        self.data = TicTacToe()
        self.data.array = ["1", "O", "2", "3", "O", "4", "5", "X", "6"]

    def test_result(self):
        ttt = self.data
        self.assertFalse(ttt.check_win(5))


class CheckWinRDiagonal1(unittest.TestCase):
    def setUp(self):
        self.data = TicTacToe()
        self.data.array = ["1", "2", "X", "3", "X", "4", "X", "6", "7"]

    def test_result(self):
        ttt = self.data
        self.assertTrue(ttt.check_win(7))


class CheckWinRDiagonal2(unittest.TestCase):
    def setUp(self):
        self.data = TicTacToe()
        self.data.array = ["1", "2", "X", "3", "X", "4", "5", "6", "7"]

    def test_result(self):
        ttt = self.data
        self.assertFalse(ttt.check_win(3))


class CheckWinLDiagonal1(unittest.TestCase):
    def setUp(self):
        self.data = TicTacToe()
        self.data.array = ["X", "O", "2", "3", "X", "5", "6", "7", "X"]

    def test_result(self):
        ttt = self.data
        self.assertTrue(ttt.check_win(5))


class CheckWinLDiagonal2(unittest.TestCase):
    def setUp(self):
        self.data = TicTacToe()
        self.data.array = ["X", "O", "2", "3", "4", "5", "6", "7", "X"]

    def test_result(self):
        ttt = self.data
        self.assertFalse(ttt.check_win(1))


class MoveCheck(unittest.TestCase):
    def setUp(self):
        self.data = TicTacToe(3, "", "1")

    def test_result(self):
        ttt = self.data
        self.assertEqual(ttt.turn, 1)

        self.assertTrue(ttt.move(1))
        self.assertEqual(ttt.turn, 2)

        self.assertFalse(ttt.move(-4))
        self.assertEqual(ttt.turn, 2)

        self.assertFalse(ttt.move(10))
        self.assertEqual(ttt.turn, 2)

        self.assertTrue(ttt.move(5))
        self.assertEqual(ttt.turn, 1)

        self.assertTrue(ttt.move(6))
        self.assertEqual(ttt.turn, 2)


if __name__ == '__main__':
    unittest.main()
