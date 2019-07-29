from models import db

def nQueens(n, board=[]):
  if len(board) == n:
    solution = Solution(
    solution = str(board),
    n = n
    )
    db.session.add(solution)
    
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


def get_all():
    solutions = Solution.query.all()
    all_solutions = []
    for x in solutions:
        new_solution = {
            "id": x.id,
            "solution": x.solution,
            "n": x.n
        }

        all_solutions.append(new_solution)
    return all_solutions