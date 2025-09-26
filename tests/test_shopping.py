from app.shopping import get_total

def test_total():
    costs = {'socks':5, 'shoes':60, 'sweater':30}
    assert get_total(costs, ['socks', 'shoes'], 0.09) == 70.85
