def get_total(costs, items, tax):
    subtotal = sum(costs.get(item, 0) for item in items)
    return round(subtotal * (1 + tax), 2)
