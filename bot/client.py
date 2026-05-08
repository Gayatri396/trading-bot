import random
import time
import logging

logger = logging.getLogger(__name__)


class BinanceClient:
    def __init__(self):
        logger.info("Mock Binance Client initialized")

    def place_order(self, params):
        """
        Simulates placing an order on Binance Futures Testnet
        """

        logger.info(f"Sending order: {params}")

        try:
            # Simulate network delay
            time.sleep(1)

            order_id = random.randint(100000, 999999)

            response = {
                "symbol": params["symbol"],
                "side": params["side"],
                "type": params["type"],
                "status": "FILLED"
                if params["type"] == "MARKET"
                else "NEW",
                "orderId": order_id,
                "executedQty": params["quantity"],
                "avgPrice": params.get("price", "65000"),
            }

            logger.info(f"Order success: {response}")

            return response

        except Exception as e:
            logger.error(f"Error placing order: {str(e)}")
            raise
