import pytest

def calculate_price_after_discount(prices, discounts):
    return [price * (1 - discount / 100) for price, discount in zip(prices, discounts)]

@pytest.mark.parametrize("prices, discounts, expected", [
    ([100, 200, 300], [10, 20, 30], [90.0, 160.0, 210.0]),
    ([50, 75, 100], [5, 10, 15], [47.5, 67.5, 85.0]),
    ([200, 300, 400], [20, 30, 40], [160.0, 210.0, 240.0]),
])
def test_calculate_price_after_discount(prices, discounts, expected):
    assert calculate_price_after_discount(prices, discounts) == expected

def test_calculate_price_after_discount_empty_lists():
    assert calculate_price_after_discount([], []) == []

def test_calculate_price_after_discount_different_list_lengths():
    with pytest.raises(ValueError):
        calculate_price_after_discount([100, 200], [10])
