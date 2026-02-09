def print_price_data(metal_name, prices):
    print(f"\n{metal_name} Price Data:")
    if not prices or prices[0] is None:
        print(f"  No price data available for {metal_name}")
        return
    
    for price in prices:
        if price is not None:
            print(f"  ${price:.2f}")

def print_trend_analysis(prices):
    if not prices or len(prices) == 0:
        print("  Trend: No data available")
        return
    valid_prices = [p for p in prices if p is not None]
    
    if len(valid_prices) == 0:
        print(" Trend: No valid price data")
        return
    
    if len(valid_prices) == 1:
        print(f"  Current Price: ${valid_prices[0]:.2f}")
        return
    if valid_prices[-1] > valid_prices[0]:
        print("Increasing")
    elif valid_prices[-1] < valid_prices[0]:
        print("Decreasing")
    else:
        print("Stable")