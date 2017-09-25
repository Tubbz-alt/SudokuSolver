# The non-yices portions of this code base come from:
#
# http://newcoder.io/gui/
#
# where the license is:
#
# https://creativecommons.org/licenses/by-sa/3.0/deed.en_US
#
# I have modified the code as I saw fit to suit my purposes.
# All changes are recorded in the git commits.
#

class SudokuBoard(object):
    """
    Sudoku Board representation
    """
    def __init__(self, board_file):
        self.board = self.__create_board(board_file)

    def __create_board(self, board_file):
        board = []
        for line in board_file:
            line = line.strip()
            if len(line) != 9:
                raise SudokuError(
                    "Each line in the sudoku puzzle must be 9 chars long."
                )
            board.append([])

            for c in line:
                if not c.isdigit():
                    raise SudokuError(
                        "Valid characters for a sudoku puzzle must be in 0-9"
                    )
                board[-1].append(int(c))

        if len(board) != 9:
            raise SudokuError("Each sudoku puzzle must be 9 lines long")
        return board
