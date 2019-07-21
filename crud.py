from sqlalchemy import create_engine
from config import DATABASE_URI
from models import Base, Solution
from sqlalchemy.orm import sessionmaker

engine = create_engine(DATABASE_URI)
# engine gives SQA the power to create tables

Session = sessionmaker(bind=engine)

def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

recreate_database()

s = Session()


def nQueens(n, board=[]):
  if len(board) == n:
    solution = Solution(
    solution = str(board)
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

nQueens(10)

s.commit()
s.close()
