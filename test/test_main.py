from app.main import add, sub


def test_addition():
    assert add(10, 5) == 15


def test_subtaction():
    assert sub(10, 5) == 5
