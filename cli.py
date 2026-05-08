import argparse
import os
import sys
from dotenv import load_dotenv

from bot.client import BinanceClient
from bot.validators import validate_inputs
from bot.orders import place_order, print_order_summary, print_order_response
from bot.logging_config import setup_logger

# Load API keys from .env file
load_dotenv()

logger = setup_logger("cli")

def get_client():
    return BinanceClient()


def main():

    side = None
    order_type = None

    print("Choose Order Side:")
    print("1. BUY")
    print("2. SELL")

    side_choice = input("Enter choice (1/2): ").strip()

    if side_choice == "1":
        side = "BUY"
    elif side_choice == "2":
        side = "SELL"
    else:
        print("Invalid choice! Exiting...")
        return


    print("\nChoose Order Type:")
    print("1. MARKET")
    print("2. LIMIT")

    type_choice = input("Enter choice (1/2): ").strip()

    if type_choice == "1":
        order_type = "MARKET"
    elif type_choice == "2":
        order_type = "LIMIT"
    else:
        print("Invalid choice! Exiting...")
        return

    symbol = input("\nEnter Symbol (e.g. BTCUSDT): ").strip().upper()

    try:
        quantity = float(input("Enter Quantity: ").strip())
    except ValueError:
        print("Invalid quantity!")
        return

    price = None

    if order_type == "LIMIT":
        try:
            price = float(input("Enter Limit Price: ").strip())
        except ValueError:
            print("Invalid price!")
            return

    try:
        symbol, side, order_type = validate_inputs(
            symbol,
            side,
            order_type,
            quantity,
            price,
        )

        print_order_summary(symbol, side, order_type, quantity, price)

        client = get_client()

        response = place_order(
            client,
            symbol,
            side,
            order_type,
            quantity,
            price,
        )

        print_order_response(response)

        logger.info("Bot finished successfully")

    except Exception as e:
        logger.error(f"Application error: {str(e)}")
        print(f"\nERROR: {str(e)}")


if __name__ == "__main__":
    main()
