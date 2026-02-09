import argparse
from cli.output_formatter import (
    print_price_data,
    print_trend_analysis
)

def get_gold_data():
    return [1000,2000,3030,4242,6767,6969]
    
def get_silver_data():
    return [22.5, 23.0, 22.8, 67.4]

def handle_command():
    def handle_command():
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
        data = get_gold_data()
        print_price_data("Gold", data)
        print_trend_analysis(data)
    elif args.metal == "silver":
        data = get_silver_data()
        print_price_data("Silver", data)
        print_trend_analysis(data)

    elif args.metal == "compare":
        gold = get_gold_data()
        silver = get_silver_data()
        print_price_data("Gold", gold)
        print_price_data("Silver", silver)
    