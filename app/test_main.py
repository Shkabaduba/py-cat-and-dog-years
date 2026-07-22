from app.main import get_human_age

def test_if_result_0():
    assert get_human_age(0, 0) == [0, 0]

def test_almost_1():
    assert get_human_age(14, 14) == [0, 0]

def test_first_human_year():
    assert get_human_age(15, 15) == [1, 1]

def test_different_age_result():
    assert get_human_age(28, 28) == [3, 2]

def test_100_years():
    assert get_human_age(100, 100) == [21, 17]

def test_does_not_exchange_cat_dog():
    assert get_human_age(24, 15) == [2, 1]

def test_first_year_cat_dog():
    assert get_human_age(23, 23) == [1, 1]

def test_second_year_cat_dog():
    assert get_human_age(24, 24) == [2, 2]
