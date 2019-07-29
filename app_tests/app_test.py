import pytest

  # solution numbers found on page 314 of https://camo.ici.ro/journal/vol19/v19b11.pdf

def test_n_results(supply_results):
    solution_numbers =	{
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
    assert supply_results[0] == solution_numbers[supply_results[1]]