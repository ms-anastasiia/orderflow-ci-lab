from orderflow.fulfillment import Basket, Line, reserve_items


def test_reserve_exact_quantity_leaves_zero_stock():
    stock = {'SKU-1': 2}
    basket = Basket(1, [Line('SKU-1', 2, 100, 'office')])
    assert reserve_items(basket, stock) is True
    assert stock['SKU-1'] == 0


def test_failed_second_line_keeps_original_stock():
    stock = {'SKU-1': 5, 'SKU-2': 1}
    before = dict(stock)
    basket = Basket(1, [
        Line('SKU-1', 2, 100, 'office'),
        Line('SKU-2', 3, 100, 'home'),
    ])
    assert reserve_items(basket, stock) is False
    assert stock == before
