import random

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
    score = getScore(board)
    print(f'Игрок ({userTile}): {score["user"]}')
    print(f'компьютер ({computerTile}): {score["computer"]}')

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

def makeMove(board: list, y: int, x: int, tile: str) -> None:
    tiles = tilesToFlip(board, y, x, tile)
    for i, j in tiles:
        board[i][j] = tile
    board[y][x] = tile

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
        i = 8 - int(s[1])
        if board[i][j] != EMPTY:
            print('Клетка занята!')
            continue
        if len(tilesToFlip(board, i, j, userTile)) == 0:
            print('Недопустимый ход: нет перевернутых фишек')
            continue
        makeMove(board, i, j, userTile)
        return

def getValidMoves(board: list, tile: str) -> list:
    ans = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == EMPTY and tilesToFlip(board, i, j, tile):
                ans.append((i, j))
    return ans

def getComputerMove(board, computerTile):
    i, j = random.choice(getValidMoves(board, computerTile))
    print('Ход компьютера: ', 'abcdefgh'[j], 8 - i, sep='')
    makeMove(board, i, j, computerTile)

def getScore(board: list) -> dict:
    ans = {'user': 0, 'computer': 0}
    for i in range(8):
        for j in range(8):
            if board[i][j] == userTile:
                ans['user'] += 1
            elif board[i][j] == computerTile:
                ans['computer'] += 1
    return ans

TILES = ['○', '●']
EMPTY = '⋅'
board = getNewBoard()
computerTile, userTile = selectUserTile()
printBoard(board)

while len(getValidMoves(board, userTile)) != 0 or len(getValidMoves(board, computerTile)) != 0:
    if len(getValidMoves(board, userTile)) != 0:
        getUserMove(board, userTile)
        printBoard(board)
    if len(getValidMoves(board, computerTile)) != 0:
        getComputerMove(board, computerTile)
        printBoard(board)
# ДЗ. Сделать подсчет очков, игровой цикл, конец игры