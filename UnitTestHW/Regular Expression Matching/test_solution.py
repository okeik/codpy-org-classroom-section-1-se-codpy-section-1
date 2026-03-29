import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()
    
testcases = [
    # s, p, expected_res
    ["", "", True],
    ["aa", "a", False],
    ["aa", "a*", True],
    ["ab", ".*", True],
    ["a", ".*.", True],
    ["aab", "c*a*b", True],
    ["aaa", "ab*a*c*a", True]
]

@pytest.mark.parametrize("s, p, expected", testcases)
def test_match(solution, s, p, expected):
    assert solution.isMatch(s, p) == expected
@pytest.mark.xfail
def test_broken_solution(solution):
    # 假設失敗的是 ["a", ".*.", True] 這組（你要自己看終端機的報錯確認是哪組）
    # 就把它寫死在這裡面
    assert solution.isMatch("a", ".*.") == True

"""
@pytest.mark.xfail
def test_broken_solution(solution):
    assert solution.isMatch() == 
"""
