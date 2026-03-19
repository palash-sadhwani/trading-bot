from binance.client import Client
import os
from dotenv import load_dotenv
import logging

load_dotenv()

class BinanceFuturesClient:
    def __init__(self):
        self.client = Client(
            os.getenv("API_KEY"),
            os.getenv("API_SECRET"),
            testnet=True  
        )

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            self.client.futures_change_leverage(symbol=symbol, leverage=10)

            params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity
            }

            if order_type == "LIMIT":
                if price is None:
                    raise ValueError("Price is required for LIMIT orders")
                params["price"] = price
                params["timeInForce"] = "GTC"

            logging.info(f"Order Params: {params}")

            response = self.client.futures_create_order(**params)

            logging.info(f"Order Response: {response}")

            return response

        except Exception as e:
            logging.error(f"Error placing order: {str(e)}")
            raise