import pytest
from api.src.queens import bishop_threatened, nQueens, checkBoard

n = 10

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

@pytest.mark.parametrize("board, addition",[([0, 2, 5],3),([2, 5, 1, 4, 7],6)])
def test_bishop_threatened(board, addition):
  assert bishop_threatened(board, addition)
  assert not bishop_threatened([0, 2, 5], 1)

@pytest.mark.parametrize("board, queen",[(validBoard,n),([2, 5, 1, 4, 7, 0, 6, 3],8)])
def test_checkBoard(board, queen):
  assert checkBoard(board, queen)
  assert not checkBoard (invalidBishopBoard, n)
  assert not checkBoard (invalidRookBoard, n)

@pytest.mark.parametrize("queen",[(4),(6),(8),(10),(12)])
def test_solution_amount(queen):
  amount = len(nQueens(queen, [], []))
  assert amount == solutionNumbers[queen]

def test_nQueens():
  solutions = nQueens(n, [], [])
  for solution in solutions:
    assert checkBoard(solution, n)

def test_api(supply_results):
  assert supply_results()

 # solution numbers found on page 314 of https://camo.ici.ro/journal/vol19/v19b11.pdf

# tests based heavily off https://github.com/cuenca-mx/clabe-python/blob/master/test_clabe.py