import pytest
from product import Product

@pytest.fixture
def product():
    return Product("Laptop", 2999.99, 10)

def test_is_available_when_in_stock(product):
    assert product.is_available() is True

def test_is_not_available_when_empty():
    empty_product = Product("Myszka", 99.99, 0)
    assert empty_product.is_available() is False

@pytest.mark.parametrize("amount, expected_quantity", [
    (5, 15),   
    (0, 10),   
    (20, 30),  
])
def test_add_stock_parametrized(product, amount, expected_quantity):
    product.add_stock(amount)
    assert product.quantity == expected_quantity

def test_add_stock_negative_raises(product):
    with pytest.raises(ValueError):
        product.add_stock(-5)

def test_remove_stock_positive(product):
    product.remove_stock(3)
    assert product.quantity == 7

def test_remove_stock_too_much_raises(product):
    with pytest.raises(ValueError):
        product.remove_stock(15)

def test_remove_stock_negative_raises(product):
    with pytest.raises(ValueError):
        product.remove_stock(-2)

def test_total_value(product):
    assert product.total_value() == pytest.approx(29999.9)

def test_init_validation():
    with pytest.raises(ValueError):
        Product("Kabel", -10.0, 5)
    with pytest.raises(ValueError):
        Product("Kabel", 10.0, -5)