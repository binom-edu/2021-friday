def getNewBoard() -> list:
    board = []
    for i in range(8):
        board.append([EMPTY] * 8)
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

def selectUserTile() -> list:
    computerTile, userTile = TILES
    s = input(f'Вы играете за "{userTile}". Сменить (y/n)? ')
    if s.lower().startswith('y'):
        computerTile, userTile = userTile, computerTile
    return [computerTile, userTile]

def inBoard(i, j) -> bool:
    return i >= 0 and i < 8 and j >= 0 and j < 8

def tilesToFlip(board: list, y: int, x: int, tile: str) -> list:
    otherTile = TILES[(TILES.index(tile) + 1) % 2]
    directions = [
        [-1, 0],
        [-1, 1],
        [0, 1],
        [1, 1],
        [1, 0],
        [1, -1],
        [0, -1],
        [-1, -1]
    ]
    ans = []
    for d in directions:
        di, dj = d
        i, j = y, x
        while True:
            i += di
            j += dj
            if not inBoard(i, j) or board[i][j] == EMPTY:
                break
            if board[i][j] == otherTile:
                continue
            i -= di
            j -= dj
            while i != y or j != x:
                ans.append((i, j))
                i -= di
                j -= dj
            break
    return ans

def getUserMove(board, userTile):
    alf = 'abcdefgh'
    while True:
        s = input('Ваш ход: ')
        if len(s) != 2:
            print('Недопустимый ввод')
            continue
        j = alf.find(s[0])
        if j == -1:
            print('Недопустимый ввод: требуется a-h')
            continue
        if not s[1] in '12345678':
            print('Недопустимый ввод: требуется цифра 1-8')
            continue
        i = int(s[1] - 1)
        if board[i][j] != EMPTY:
            print('Клетка занята!')
            continue
        # проверить, что ход допустимый (есть что переворачивать)


TILES = ['○', '●']
EMPTY = '⋅'
board = getNewBoard()
printBoard(board)
computerTile, userTile = selectUserTile()