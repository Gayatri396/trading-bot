from bot.client import BinanceClient
from bot.logging_config import setup_logger

logger = setup_logger("orders")


def place_order(client: BinanceClient, symbol: str, side: str, order_type: str, quantity: float, price: float = None) -> dict:
    """
    Builds the order parameters and sends them to Binance via the client.
    Returns the full response from Binance.
    """

    # --- Build the order params ---
    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
    }

    # Price is only added for LIMIT orders
    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"  # GTC = Good Till Cancelled

    # --- Log what we're about to send ---
    logger.info(f"Order Request : {side} {order_type} | Symbol: {symbol} | Qty: {quantity}" +
                (f" | Price: {price}" if price else ""))

    # --- Send to Binance ---
    response = client.place_order(params)

    # --- Log the response ---
    logger.info(f"Order Response : OrderID: {response.get('orderId')} | "
                f"Status: {response.get('status')} | "
                f"ExecutedQty: {response.get('executedQty')} | "
                f"AvgPrice: {response.get('avgPrice')}")

    return response


def print_order_summary(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    """
    Prints a clean summary of what order is being placed — before sending.
    """
    print("\n" + "="*50)
    print("ORDER REQUEST SUMMARY")
    print("="*50)
    print(f"  Symbol     : {symbol}")
    print(f"  Side       : {side}")
    print(f"  Order Type : {order_type}")
    print(f"  Quantity   : {quantity}")
    if price:
        print(f"  Price      : {price}")
    print("="*50 + "\n")


def print_order_response(response: dict):
    """
    Prints a clean summary of what Binance returned after placing the order.
    """
    print("\n" + "="*50)
    print("ORDER RESPONSE")
    print("="*50)
    print(f"  Order ID     : {response.get('orderId', 'N/A')}")
    print(f"  Symbol       : {response.get('symbol', 'N/A')}")
    print(f"  Status       : {response.get('status', 'N/A')}")
    print(f"  Side         : {response.get('side', 'N/A')}")
    print(f"  Type         : {response.get('type', 'N/A')}")
    print(f"  Quantity     : {response.get('origQty', 'N/A')}")
    print(f"  Executed Qty : {response.get('executedQty', 'N/A')}")
    print(f"  Avg Price    : {response.get('avgPrice', 'N/A')}")
    print("="*50)
    print("Order placed successfully!")
    print("="*50 + "\n")
