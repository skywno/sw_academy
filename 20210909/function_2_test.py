import pytest

from function_2 import rock_paper_scissor


def test_rock_wins_scissor():
    assert rock_paper_scissor("바위", "가위") == "바위가 이겼습니다!"


def test_rock_loses_to_paper():
    assert rock_paper_scissor("바위", "보") == "보가 이겼습니다!"
