gameState = {
  "board" : [], # array of arrays, [0][0] is top left, [7][7] is bottom right
  "nextMove" : "w",
  "castling" : "KQkq", # k means kingside, q means queenside, uppercase is white and lowercase is black, a dash indicates no castling available
  "passant" : "-", # the target square in algabreic notation, this is the square "behind" the pawn
  "halfClock" : 0, # the number of half-moves since the last capture or pawn move, used for the fifty-move tie rule
  "fullmoveNum" : 1 # the number of the full move, incremented after black's move
}

# piece representations (white is uppercase, black is lowercase):
# empty: -
# pawn: P
# knight: N
# bishop: B
# rook: R
# queen: Q
# king: K

def importFEN(fenString): # turn a FEN string into a game state dictionary
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
  return {"board" : newBoard, "nextMove" : segments[1], "castling" : segments[2], "passant" : segments[3], "halfClock" : int(segments[4]), "fullmoveNum" : int(segments[5])}

def exportFEN(gameState): #turn a game state dictionary into a FEN string
  boardString = ""
  for rank in gameState["board"]:
    numEmpty = 0 # count number of empty spaces in a row
    for file in rank:
      if (file == "-"):
        numEmpty = numEmpty + 1
      else:
        if (numEmpty != 0):
          boardString = boardString + str(numEmpty)
          numEmpty = 0
        boardString = boardString + file
    if (numEmpty != 0):
      boardString = boardString + str(numEmpty)
    boardString = boardString + "/"
  boardString = boardString[0:-1] # remove last slash using slicing
  
  return boardString + " " + gameState["nextMove"] + " " + gameState["castling"] + " " + gameState["passant"] + " " + str(gameState["halfClock"]) + " " + str(gameState["fullmoveNum"])

def standardLocToPos(location): # converts a location like "e2" into it's code representation of [4,6]
  file = ord(location[0:1])-97
  rank = 8-int(location[1:2])
  return [rank,file]

def doMove(gameState,move):
  if (move == "O-O"): # TODO: implement castling
    print("Castle kingside")
  elif (move == "O-O-O"):
    print("Castle queenside")
  else:
    pieceType = move[0:1]
    startLocation = standardLocToPos(move[1:3])
    if (move[3:4] == "x"):
      endLocation = standardLocToPos(move[4:6])
    else:
      endLocation = standardLocToPos(move[3:5])
    gameState["board"][endLocation[0]][endLocation[1]] = pieceType
    gameState["board"][startLocation[0]][startLocation[1]] = "-"
  if (gameState["nextMove"] == "w"): # flip the next player to move
    gameState["nextMove"] = "b"
  else:
    gameState["nextMove"] = "w"
    gameState["fullmoveNum"] = gameState["fullmoveNum"] + 1 # increment the number of full moves after black makes a move
  if (move.lower()[0:1] == "p" or move[3:4] == "x"): # check if a capture has occurred or a pawn has advanced for the 50-move tie rule
    gameState["halfClock"] = 0
  else:
    gameState["halfClock"] = gameState["halfClock"] + 1
  return gameState
    

gameState = importFEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

print(exportFEN(gameState))

print("Pe2e4")
gameState = doMove(gameState,"Pe2e4")
print(exportFEN(gameState))

print("pd7d6")
gameState = doMove(gameState,"pd7d6")
print(exportFEN(gameState))

print("Bf1b5")
gameState = doMove(gameState,"Bf1b5")
print(exportFEN(gameState))
