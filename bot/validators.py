from bot.logging_config import setup_logger

logger = setup_logger("validators")

VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]


def validate_inputs(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    """
    Checks all user inputs before sending to Binance.
    Raises ValueError with a clear message if anything is wrong.
    """

    # 1. Check symbol
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Symbol is required! Example: BTCUSDT")
    symbol = symbol.upper().strip()
    if len(symbol) < 3:
        raise ValueError(f"Symbol '{symbol}' looks invalid! Example: BTCUSDT")

    # 2. Check side
    side = side.upper().strip()
    if side not in VALID_SIDES:
        raise ValueError(f"Side must be BUY or SELL. You entered: '{side}'")

    # 3. Check order type
    order_type = order_type.upper().strip()
    if order_type not in VALID_ORDER_TYPES:
        raise ValueError(f"Order type must be MARKET or LIMIT. You entered: '{order_type}'")

    # 4. Check quantity
    if quantity is None:
        raise ValueError("Quantity is required!")
    if quantity <= 0:
        raise ValueError(f"Quantity must be greater than 0. You entered: {quantity}")

    # 5. Check price (only required for LIMIT orders)
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders! Example: --price 60000")
        if price <= 0:
            raise ValueError(f"Price must be greater than 0. You entered: {price}")

    logger.info(f"Inputs validated - {side} {order_type} | {symbol} | Qty: {quantity}" +
                (f" | Price: {price}" if price else ""))

    return symbol, side, order_type
