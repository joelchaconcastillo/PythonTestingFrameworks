from hypothesis import given, strategies as st

@given(st.integers(), st.integers())
def test_addition_commutative(a, b):
    result1 = a + b
    result2 = b + a
    assert result1 == result2

