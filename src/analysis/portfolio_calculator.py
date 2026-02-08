def calculate_portfolio_value(transactions, current_prices):
    """
    går igenom alla transaktioner och räknar ut totalvärdet
    baserat på aktuella priser.
    """
    total_value = 0
    for t in transactions:
        # //Vi antar att 't' har attributen 'metal_name' och 'amount'
        price = current_prices.get(t.metal_name, 0)
        total_value += t.amount * price
    return total_value

def calculate_roi(initial_investment, current_value):
    """räknar ut Return on Investment."""
    if initial_investment == 0:
        return 0
    return ((current_value - initial_investment) / initial_investment) * 100