
def nQueens(n, board=[], results=[]):
  if len(board) == n:
    if checkBoard(board, n):
      results.append(board)
    
  for c in set(range(n)) - set(board):
    # this also checks for rook threats as it takes out what is already present in the board
    if not bishop_threatened (board, c):
      nQueens(n, board + [c], results)

  return results
# nQueens code partially based off  http://code.activestate.com/recipes/576647-eight-queens-six-lines/?fbclid=IwAR2agAgxDON-HRZieQm3hcSfXRIcho0PStTml6uScNrs-McgXf7nydvyZaM
# but mostly based off my own solution in javascript that I wrote during HolaCode

def bishop_threatened (board, newRow):
  s = len(board)
  cols = range(s)
  
  for i in cols:
    if s - i == abs(newRow-board[i]):
      return True
  return False

def checkBoard(board, n):
  s = len(board)
  cols = range(s)

  if (s == n 
        == len(set(board[i]+i for i in cols))
        == len(set(board[i]-i for i in cols))):
        return True

