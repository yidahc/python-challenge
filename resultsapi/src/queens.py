
def nQueens(n, board=[], results=[]):
  # base case: if board is full, we can end this recursive call
  if len(board) == n:
    # double checking the board we built recursively is threat-free (really not neccessary, but better safe than sorry)
    if checkBoard(board, n):
      # add board to results
      results.append(board) 

  # recursive case: iterates through n, minus values already present in the board we are currently building
  # which also checks for rook threats (set also checks for duplicates), eliminating any horizontal threats
  for c in set(range(n)) - set(board):
    # if adding potential new column index to the existing board will be threatened diagonally, 
    # loop continues to check next possible addition. 
    # if there is no valid addition to this board, loop exists and starts building new board
    if not bishop_threatened (board, c):
      # add unthreatened new column placement and continue to build board
      nQueens(n, board + [c], results)

  return results

# checks for possible diagonal threats before adding new column placement to board
def bishop_threatened (board, newCol):
  # size of the board we are currently building
  # if test passes, this will be the index (row placement) of the new column placement
  r = len(board)
  # the rows (indexes) we have built so far
  rows = range(r)
  
  for i in rows: # iterate through board rows (indexes in list)
    # compares the distance between new potential row placement (index) and row placement (index) we are currently iterating on (new row will always be higher than row we are on, so abs is not needed)
    # and the distance between the new column placement (value) we want to add and the columnn placement (value) of the row index we are on
    if r - i == abs(newCol-board[i]):
      # if row and column distances are the same, they are diagonal from each other (like making a square) and pose a threat
      return True
  # return false once we are done checking all current placements against threat from new placement
  return False

# backup function to check a finished board is a valid solution for the given n
def checkBoard(board, n):
  s = len(set(board)) # length of board once checked for duplicates
  cols = range(s)

  if (s == n # once checked for horizontal/rook threats, checks board is still complete by comparing to n
        # iterates through board and adds/subtracts row placement (index) and column placement (value) 
        # while eliminating any duplicate results with set (duplicate results are bishop threats to each other)
        == len(set(board[i]+i for i in cols)) 
        # ex : [2,5,0,6,1,3] => board[i]+i => 2,6,2,9,5,8 => (0,2) and (2,0) are diagonal threats
        == len(set(board[i]-i for i in cols))):
        # ex2: [6,3,4,2,5] => board[i]-i => 6,2,2,-1,1 => (1,3) and (2,4) are diagonal threats
             # [6,3,4,2,5] => board[i]+i => 6,4,6,5,9  => (0,6) and (2,4) are diagonal threats
        # once checked for diagonal/bishop threats, if len(set)==n then board is a valid and complete threat-free solution
        return True
  # if any check fails, it is not a valid solution
  return False

print (nQueens(4))
# checkBoard from http://code.activestate.com/recipes/576647-eight-queens-six-lines/?fbclid=IwAR2agAgxDON-HRZieQm3hcSfXRIcho0PStTml6uScNrs-McgXf7nydvyZaM
