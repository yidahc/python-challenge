
def nQueens(n, board=[], results=[]):
  # base case: if board is full, we can end this recursive call
  if len(board) == n:
    if checkBoard(board, n):
    # double checking the board we built recursively is threat-free (really not neccessary, but better safe than sorry)
      results.append(board)
      # convert board to matrix and add to results

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
  r = len(board)
  # size of the board we are currently building
  # if test passes, this will be the index (row placement) of the new column placement
  rows = range(r)
   # the rows (indexes) we have built so far
  
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
        # this one tests for minor diagonal threats (top right down to bottom left corner)
        # ex : [2,5,0,6,1,3] => board[i]+i => 2,6,2,9,5,8 => (0,2) and (2,0) are diagonal threats
             # [6,3,4,2,5] => board[i]+i => 6,4,6,5,9  => (0,6) and (2,4) are diagonal threats
        == len(set(board[i]-i for i in cols))):
        # this one tests for major diagonal threats (top left down to bottom right corner)
        # ex2: [6,3,4,2,5] => board[i]-i => 6,2,2,-1,1 => (1,3) and (2,4) are diagonal threats
        # once checked for diagonal/bishop threats, if len(set)==n then board is a valid and complete threat-free solution
        return True
  # if any check fails, it is not a valid solution
  return False


def matrixBoards (board):
  newBoard = [] 
  queens = len(board) # amount of queens == N
  S = range(queens)  # size of matrix (NxN)

  for queen in board: # looping through board (first iteration over N)
    # each queen value stands for its placement in its row (its column index on its new row)
    newRow = []
    # creating a new newRow for each queen in board (creating N rows)
    for c in S:
    # second iteration over N to add N columns in each row
      if c != queen:
      # if the column we are adding is not where a queen should be
        newRow.append(0)
        # build column by adding a 0 (empty spot) to row we are building
      else:
      # if the column we are adding is where this row's queen placement is 
        newRow.append(1)
        # place a queen there instead (represented by 1)
    newBoard.append(newRow)    
    # adding each new row to matrix
  return newBoard

# function to convert single list boards into a nested list matrix
def convertBoard (board):
  N = len(board) # size of matrix (NxN)
  S = range(N)
  newBoard = [] + [[]] * N # creating matrix with N amount of rows

  for i in S: # iterate through N to fill empty rows
    newRow = [0] * N # creating a new row for each queen in board, with N amount of empty spaces
    newRow[board[i]] = 1 # placing queen in new row at its 
    newBoard[i] = newRow
  # needs to refer to index of this queen
  return newBoard

print (convertBoard([1, 3, 0, 2]))