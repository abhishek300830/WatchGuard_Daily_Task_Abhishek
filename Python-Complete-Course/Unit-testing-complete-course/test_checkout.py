import pytest

from Checkout import Checkout


@pytest.fixture()
def checkout():
    checkout = Checkout()
    return checkout


def test_can_instantiated_checkout():
    co = Checkout()


def test_can_add_item_price(checkout):
    checkout.add_item_price("a", 1)


def test_can_add_item(checkout):
    # checkout.add_item("")
    pass


def test_can_calculate_total(checkout):
    checkout.add_item_price("b", 2)
    checkout.add_item("b")
    assert checkout.calculate_area() == 2


def test_get_correct_total_with_multiple_items(checkout):
    checkout.add_item_price("c", 1)
    checkout.add_item_price("d", 2)
    checkout.add_item("c")
    checkout.add_item("d")
    assert checkout.calculate_area() == 3


def test_can_add_discount_rule(checkout):
    checkout.add_discount("a", 3, 2)


def test_exception_with_bad_item(checkout):
    with pytest.raises(Exception):
        checkout.add_item("C")
