from config import Session
from models import Solution
import pytest

@pytest.fixture
def supply_results():
  s = Session()
  
  last_solution = s.query(Solution).order_by(Solution.id.desc()).first()

  s.close()
  return [last_solution.id, last_solution.n]


# pytest learned from https://docs.pytest.org/en/latest/getting-started.html#getstarted
# and https://www.guru99.com/pytest-tutorial.html?fbclid=IwAR2BRdcMLu4TUe5QwbC5fQFSb4le2y9zgUXX3yEsxuuRosBzgfl402-CyHg