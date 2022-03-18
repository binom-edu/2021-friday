from subprocess import list2cmdline


def getNewBoard() -> list:
    board = []
    for i in range(8):
        board.append(['⋅'] * 8)
    board[3][3] = TILES[1]
    board[4][4] = TILES[1]
    board[3][4] = TILES[0]
    board[4][3] = TILES[0]
    return board

def printBoard(board):
    print('  a b c d e f g h')
    for i in range(8):
        print(8 - i, ' ', ' '.join(board[i]), ' ', 8 - i, sep='')
    print('  a b c d e f g h ')

TILES = ['○', '●']
board = getNewBoard()
printBoard(board)