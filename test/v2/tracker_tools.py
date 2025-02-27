from polygonscan_api import PolygonscanAPI

def get_token_transactions(api_key, address):
    api = PolygonscanAPI(api_key)
    return api.get_token_transactions(address)['result']

def get_non_zero_balances(api_key, address):
    api = PolygonscanAPI(api_key)

    # Fetch token transactions for the given wallet address.
    token_transactions = api.get_token_transactions(address)

    # Collect and filter unique non-zero balances across different tokens
    token_balances = {}
    for tx in token_transactions['result']:
        if int(tx['value']) != 0: 
            contract_address = tx['contractAddress']
            value = int(tx['value'])
            
            if contract_address not in token_balances:
                token_balances[contract_address] = {
                    'balance': 0,
                    'decimals': int(tx['tokenDecimal']),
                    'transactions_count': 1,
                    'tokenName': tx.get('tokenName', '-'),
                    'tokenSymbol': tx.get('tokenSymbol', '-')
                }

            # Update balance based on transaction direction
            if tx['from'].lower() == address.lower():
                token_balances[contract_address]['balance'] -= value
            else:
                token_balances[contract_address]['balance'] += value

            token_balances[contract_address]['transactions_count'] += 1

        # Filter out tokens with zero balance or negative balances since they are invalid for this use case.
        non_zero_tokens = {addr: data for addr, data in token_balances.items() if data['balance'] > 0}

    return non_zero_tokens

def get_token_balances_with_metadata(api_key, wallet_address):
    token_balances = get_non_zero_balances(api_key, wallet_address)

    result = [
        {
            "token_address": addr,
            "balance": str(data['balance']),
            "decimals": data['decimals'],
            "transactions_count": str(data['transactions_count']),
            "token_name": data['tokenName'],
            "token_symbol": data['tokenSymbol']
        }
        for addr, data in token_balances.items()
    ]

    return result

def convert_wei_to_decimal(value, decimals):
    return int(value) / (10 ** decimals)