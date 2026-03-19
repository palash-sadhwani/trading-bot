import argparse
import logging
from client.binance_client import BinanceFuturesClient

logging.basicConfig(
    filename="logs/bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        client = BinanceFuturesClient()

        print("\nOrder Request:")
        print(vars(args))

        response = client.place_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        logging.info(f"Order Response: {response}")

        print("\nOrder Success:")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        print("\nOrder Failed:", str(e))


if __name__ == "__main__":
    main()