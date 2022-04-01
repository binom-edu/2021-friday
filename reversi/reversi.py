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

def selectUserTile() -> list:
    computerTile, userTile = TILES
    s = input(f'Вы играете за "{userTile}". Сменить (y/n)? ')
    if s.lower().startswith('y'):
        computerTile, userTile = userTile, computerTile
    return [computerTile, userTile]

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
            if ...



TILES = ['○', '●']
board = getNewBoard()
printBoard(board)
computerTile, userTile = selectUserTile()