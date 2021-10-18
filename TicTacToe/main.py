
"""
This is simple TicTacToe with not defined size
"""


class TicTacToe:

    def __init__(self, size=3, player1="player1", player2="player2"):
        size = abs(size)
        self.size = size
        if player1 == player2:
            raise UserWarning("names must be different")
        self.player1 = player1
        self.player2 = player2
        self.turn = 1
        self.array = list(range(1, size**2 + 1))

    # O(1)
    def move(self, position):
        if position > self.size**2 or position < 1:
            return False

        if self.array[position - 1] != position:
            return False

        if self.turn == 1:
            self.array[position - 1] = "X"
            self.turn = 2
        else:
            self.array[position - 1] = "O"
            self.turn = 1
        return True

    # O(n)
    def __check_line(self, position):
        line = (position - 1) // self.size
        symbol = self.array[self.size * line]
        for i in range(1, self.size):
            if self.array[line * self.size + i] != symbol:
                return False
        return True

    # O(n)
    def __check_column(self, position):
        col = (position - 1) % self.size
        symbol = self.array[col]
        for i in range(1, self.size):
            if self.array[col + i * self.size] != symbol:
                return False
        return True

    # O(n)
    def __check_diagonal(self, position):
        if position % (self.size + 1) == 1:
            symbol = self.array[0]
            for i in range(self.size + 1, self.size * self.size + 1, self.size + 1):
                if self.array[i] != symbol:
                    return False
            return True
        if (position - 1) % self.size + (position - 1) // self.size == self.size - 1:
            symbol = self.array[self.size - 1]
            for i in range(self.size - 1, self.size * (self.size - 1) + 1, self.size - 1):
                if self.array[i] != symbol:
                    return False
            return True
        return False

    # O(n)
    def check_win(self, position):
        if self.__check_line(position) or self.__check_column(position) \
                or self.__check_diagonal(position):
            return True
        return False

    # O(n**2)
    def print_table(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.array[i * self.size + j], end='')
                if j != self.size - 1:
                    print("|", end='')
            if i != self.size - 1:
                print("\n" + (self.size * 2 - 1) * "-")
        print()

    @staticmethod
    def get_uint():
        inp = input()
        if inp.isdigit():
            inp = int(inp)
            return inp
        return None


def start_game():
    ttt = TicTacToe()
    print("Choose size of table::")
    size = ttt.get_uint()
    if not size:
        return
    print("player1 name::")
    player1 = input()
    print("player2 name::")
    player2 = input()
    ttt = TicTacToe(size, player1, player2)
    ttt.print_table()
    i = 0
    while True:
        print("Enter position(cmd-D to exit)::")

        position = ttt.get_uint()

        if not position:
            continue

        if not ttt.move(position):
            print("position has already used or out of range")
            continue

        if ttt.check_win(position):
            break
        ttt.print_table()
        print()
        i += 1
        if i == ttt.size**2:
            print("Draw")
            ttt.turn = 3
            break
    if ttt.turn == 2:
        print(f"\n {ttt.player1} Wiiiin!!!")
    elif ttt.turn == 1:
        print(f"\n {ttt.player2} Wiiiin!!!")


if __name__ == '__main__':
    while True:
        try:
            start_game()
        except UserWarning as s_err:
            print(f"{s_err}, so program will be started again")
        except EOFError as s_err:
            print("god buy!")
            break
        except KeyboardInterrupt as s_err:
            print(s_err)
            break
