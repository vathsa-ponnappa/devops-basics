import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from app.main import add,sub


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(5, 3) == 2
