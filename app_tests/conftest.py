from ..resultsAPI import src
from src import Session, Solution
import pytest
# importing learned here https://stackoverflow.com/questions/20075884/python-import-module-from-another-directory-at-the-same-level-in-project-hierar
# and here https://docs.python.org/2/tutorial/modules.html#intra-package-references

@pytest.fixture
def supply_results():
  s = Session()
  
  last_solution = s.query(Solution).order_by(Solution.id.desc()).first()

  s.close()
  return [last_solution.id, last_solution.n]


# pytest learned from https://docs.pytest.org/en/latest/getting-started.html#getstarted
# and https://www.guru99.com/pytest-tutorial.html?fbclid=IwAR2BRdcMLu4TUe5QwbC5fQFSb4le2y9zgUXX3yEsxuuRosBzgfl402-CyHg