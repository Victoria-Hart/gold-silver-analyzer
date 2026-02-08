def compare_prices(metal_a_price, metal_b_price):
    """Jämför priset mellan två metaller och returnerar kvoten."""
    if metal_b_price == 0:
        return 0
    return metal_a_price / metal_b_price

def get_price_difference_percent(old_price, new_price):
    """Räknar ut procentuell förändring."""
    if old_price == 0:
        return 0
    return ((new_price - old_price) / old_price) * 100