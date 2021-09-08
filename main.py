gameState = {
  board = [], # array of arrays, (0,0) is top left, (7,7) is bottom right
  nextMove = "w",
  castling = "KQkq", # k means kingside, q means queenside, uppercase is white and lowercase is black, a dash indicates no castling available
  passant = "-", # the target square in algabreic notation, this is the square "behind" the pawn
  halfClock = 0, # the number of moves since the last capture or pawn move, used for the fifty-move tie rule
  fullmoveNum = 1 # the number of the full move, incremented after black's move
}

# piece representations (white is uppercase, black is lowercase):
# empty: -
# pawn: P
# knight: N
# bishop: B
# rook: R
# queen: Q
# king: K

def importFEN(fenString):
  # split the FEN string into it's individual pieces
  segments = fenString.split(" ")
  ranks = segments[0].split("/")
  
  newBoard = [] # empty the board before every import
  for rank in range(8):
    newBoard.append([]) # new array for each rank
    for c in ranks[rank]:
      if (c.isdigit()): # numbers in a FEN string indicate that many blank spaces
        for i in range(int(c)):
          newBoard[rank].append("-")
      else:
        newBoard[rank].append(c)
  return {board = newBoard, nextMove = segments[1], castling = segments[2], passant = segments[3], halfClock = segments[4], fullmoveNum = segments[5]}

print(gameState)

gameState = importFEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

print(gameState)
