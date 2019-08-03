import pytest
import requests
from front-end import RESULTS_API_SERVER
from 

# importing learned here https://stackoverflow.com/questions/20075884/python-import-module-from-another-directory-at-the-same-level-in-project-hierar
# and here https://docs.python.org/2/tutorial/modules.html#intra-package-references

@pytest.fixture
def supply_results():

  json = {
          'n': '10'
      }
  response = requests.post(RESULTS_API_SERVER + "/add", json=json)
  if response.status_code == 200:
    solutions = requests.get(RESULTS_API_SERVER + "/show").json()  
      for solution in solutions:
        return solution

@pytest.fixture
def supply_last_result():
  
  last_solution = s.query(Solution).order_by(Solution.id.desc()).first()

  return last_solution



# pytest learned from https://docs.pytest.org/en/latest/getting-started.html#getstarted
# and https://www.guru99.com/pytest-tutorial.html?fbclid=IwAR2BRdcMLu4TUe5QwbC5fQFSb4le2y9zgUXX3yEsxuuRosBzgfl402-CyHg