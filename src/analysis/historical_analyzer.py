def calculate_average(price_list):
    """Räknar ut snittpriset från en lista med historiska priser."""
    if not price_list:
        return 0
    return sum(price_list) / len(price_list)

def identify_trend(price_list):
    """Ser om trenden är uppåtgående eller nedåtgående."""
    if len(price_list) < 2:
        return "Ingen trend tillgänglig"
    
    if price_list[-1] > price_list[0]:
        return "Uppåtgående"
    elif price_list[-1] < price_list[0]:
        return "Nedåtgående"
    return "Stabil"