from results-api import queens
from queens import bishop_threatened, nQueens, checkBoard

n = 10

partialBoard = [0, 2, 5]

validAddition = 1

threatenedAddition = 3

validBoard = [5, 8, 2, 0, 3, 6, 9, 1, 4, 7]

invalidRookBoard = [3, 7, 2, 8, 6, 9, 8, 5, 1, 4]

invalidBishopBoard = [7, 3, 1, 6, 3, 5, 0, 8, 4, 2]

solutionNumbers =	{
    0: 0,
    1: 1,
    2: 0,
    3: 0,
    4: 2,
    5: 10,
    6: 4,
    7: 40,
    8: 92,
    9: 352,
    10: 724,
    11: 2680,
    12: 14200
    }

def test_bishop_threatened():
  assert bishop_threatened(partialBoard, threatenedAddition)
  assert not bishop_threatened(partialBoard, validAddition)
  
def test_checkBoard():
  assert checkBoard(validBoard, n)
  assert not checkBoard (invalidBishopBoard, n)
  assert not checkBoard (invalidRookBoard, n)

def test_solution_amount():
  amount = len(nQueens(n, [], []))
  assert amount == solutionNumbers[n]

def test_nQueens():
  solutions = nQueens(n, [], [])
  for solution in solutions:
    assert checkBoard(solution)


 # solution numbers found on page 314 of https://camo.ici.ro/journal/vol19/v19b11.pdf
