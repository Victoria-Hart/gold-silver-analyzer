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
        choices=["gold", "silver", "compare"],
        help="Metal to analyze"
    )

    args = parser.parse_args()

    if args.metal == "gold":
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
        gold_price = client.get_price("XAU")
        silver_price = client.get_price("XAG")

        if gold_price is not None:
            print_price_data("Gold", [gold_price])
        if silver_price is not None:
            print_price_data("Silver", [silver_price])