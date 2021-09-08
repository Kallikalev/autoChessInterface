board = []

# set up empty board
for rank in range(8):
  board.append([])
  for file in range(8):
    board[rank].append(0)

print(board)
