def test_smoke():
    """Simple smoke test to verify pytest runs successfully."""
    assert True

def test_addition():
    """Check simple arithmetic"""
    result = 2 + 3
    assert result == 5

def test_string():
    """Validate string operations"""
    name = "vathsa".capitalize()
    assert name == "Vathsa"
