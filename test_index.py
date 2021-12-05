from index import find_repeat
def test_find_repeat():
    numbers = ["2124443321", "2158861321", 
           "8564659988", "3121100845",
           "8564659988", "2124443321"]
    assert find_repeat(numbers) == {"2124443321": [0, 5], "8564659988": [2, 4]}