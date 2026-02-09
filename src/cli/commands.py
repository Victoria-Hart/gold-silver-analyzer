import argparse
from cli.output_formatter import (
    print_price_data,
    print_trend_analysis
)

def handle_command(client):
    parser = argparse.ArgumentParser(
        description="Gold & Silver Price Analyzer"
    )

    parser.add_argument(
        "metal",
        choices=["gold", "silver", "compare", "all"],
        help="Metal to analyze"
    )

    args = parser.parse_args()

    # LOOP 
    if args.metal == "all":
        metals = {
            "Gold": "XAU",
            "Silver": "XAG"
        }
        
        # ÄLSKAR LOOPS
        for metal_name, metal_code in metals.items():
            price = client.get_price(metal_code)
            prices = [price] if price is not None else []
            print_price_data(metal_name, prices)
            print_trend_analysis(prices)
            print("-" * 40)  # 
    
    elif args.metal == "gold":
        price = client.get_price("XAU")
        prices = [price] if price is not None else []
        print_price_data("Gold", prices)
        print_trend_analysis(prices)

    elif args.metal == "silver":
        price = client.get_price("XAG")
        prices = [price] if price is not None else []
        print_price_data("Silver", prices)
        print_trend_analysis(prices)

    elif args.metal == "compare":
        # ANOTHER LOOP
        metals_to_compare = [
            ("Gold", "XAU"),
            ("Silver", "XAG")
        ]
        
        for metal_name, metal_code in metals_to_compare:
            price = client.get_price(metal_code)
            if price is not None:
                print_price_data(metal_name, [price])