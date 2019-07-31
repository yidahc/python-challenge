<<<<<<< HEAD
<<<<<<< HEAD:results-api/src/crud.py
from models import db
=======
from models import Solution
from config import Session, recreate_database

recreate_database()

s = Session()

>>>>>>> 7bb58e5b63877f8df77406a97ec4bfe104cb0c16:crud.py
=======
>>>>>>> dockerCompose

def nQueens(n, board=[], results = []):
  if len(board) == n:
    results.append(board)
    
  for c in set(range(n)) - set(board):
    if not threatened (board, c):
      nQueens(n, board + [c], results)
  
  return results

# nQueens code partially based off last code in the comments on http://code.activestate.com/recipes/576647-eight-queens-six-lines/?fbclid=IwAR2agAgxDON-HRZieQm3hcSfXRIcho0PStTml6uScNrs-McgXf7nydvyZaM
# but mostly based off my own solution in javascript that I wrote during HolaCode

def threatened (board, newRow):
  s = len(board)
  cols = range(s)
  
  for i in cols:
    if s - i == abs(newRow-board[i]):
      return True
  return False

print (nQueens(int(8)))

