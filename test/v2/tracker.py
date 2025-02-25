import os
from dotenv import load_dotenv

from tracker_tools import convert_wei_to_decimal

class WalletAddressTracker:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("POLYGONSCAN_API_KEY")
        self.wallet_address = os.getenv("WALLET_ADDRESS")

    def track_token_balances(self):
        from tracker_tools import get_token_balances_with_metadata

        balance_info = get_token_balances_with_metadata(self.api_key, self.wallet_address)

        if not balance_info:
            return "No token balances found for the specified wallet address."

        result_str = "\n".join([
            f"Token Address: {info['token_address']}"
            f" - Token Name: {info['token_name']}"
            f" - Token Symbol: {info['token_symbol']}"
            f" - Balance: {convert_wei_to_decimal(info['balance'], info['decimals'])} ({info['transactions_count']} transactions)"
            for info in balance_info
        ])

        return result_str

if __name__ == "__main__":
    tracker = WalletAddressTracker()
    print(tracker.track_token_balances())