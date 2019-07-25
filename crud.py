from models import Base, Solution
from config import Session, recreate_database

recreate_database()

s = Session()


def nQueens(n, board=[]):
  if len(board) == n:
    solution = Solution(
    solution = str(board),
    n = n
    )
    s.add(solution)

  for c in set(range(n)) - set(board):
    if not threatened (board, c):
      nQueens(n, board + [c])


def threatened (board, newRow):
  s = len(board)
  cols = range(s)
  
  for i in cols:
    if s - i == abs(newRow-board[i]):
      return True
  return False

queensN = input("Enter N:")
nQueens(int(queensN))

s.commit()
s.close()
