import requests

API_KEY = 'YourApiKeyToken'
ADDRESS = 'YourAddress'

# 1. Get Ether Balance
eth_balance_url = f"https://api.polygonscan.com/api?module=account&action=balance&address={ADDRESS}&apikey={API_KEY}"
eth_response = requests.get(eth_balance_url)
eth_balance = eth_response.json()

# 2. Get Token Transactions
token_tx_url = f"https://api.polygonscan.com/api?module=account&action=tokentx&address={ADDRESS}&startblock=0&endblock=99999999&page=1&offset=100&sort=asc&apikey={API_KEY}"
token_tx_response = requests.get(token_tx_url)
token_transactions = token_tx_response.json()

# 3. Get Token Balances for each token from transactions
token_balances = []
for tx in token_transactions['result']:
    contract_address = tx['contractAddress']
    token_balance_url = f"https://api.polygonscan.com/api?module=account&action=tokenbalance&contractaddress={contract_address}&address={ADDRESS}&tag=latest&apikey={API_KEY}"
    token_balance_response = requests.get(token_balance_url)
    token_balances.append(token_balance_response.json())

# Final output
print("ETH Balance:", eth_balance)
print("Token Balances:", token_balances)