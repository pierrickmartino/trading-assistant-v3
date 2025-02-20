from polygonscan_api import get_balance, get_token_transfers, get_token_balances
from tracker_tools import parse_token_transfers, convert_wei_to_decimal
import os

def main(wallet_address):

    print(f"Tracking tokens for wallet: {wallet_address}\n")

    # Get POL balance
    pol_balance = get_balance(wallet_address)
    pol_balance_eth = convert_wei_to_decimal(pol_balance, 18)
    
    print(f"POL Balance: {pol_balance_eth} ETH")

    # Fetch token transfers
    transfers = get_token_transfers(wallet_address)
    if transfers:
        tokens = parse_token_transfers(transfers)
        for token in tokens:
            balance = get_token_balances(wallet_address, token['contractAddress'])
            decimal_value = convert_wei_to_decimal(balance, token['decimals'])
            if decimal_value > 0:
                print(f"Token: {token['tokenName']} ({token['tokenSymbol']}), Balance: {decimal_value}")
    else:
        print("No token transfers found or an error occurred.")

if __name__ == "__main__":
    address = input("Enter the wallet address: ")
    main(address)