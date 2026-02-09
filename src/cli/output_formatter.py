def print_price_data(metal,prices):
    print(f"\n{metal} Price Data:")
    for i, price in enumerate(prices, start=1)
        print(f" Day {i}: {price}")
def print_trend_analysis(prices):
    if prices[-1] < prices[0]:
        trend = "upward"
    elif prices[-1] < prices[0]:
        trend = "downward "
    else:
        trend = "stable "

    print(f" Trend: {trend}")