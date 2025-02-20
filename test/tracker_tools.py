def parse_token_transfers(transfers):
    tokens = {}
    for transfer in transfers:
        contract = transfer['contractAddress']
        if contract not in tokens:
            tokens[contract] = {
                'tokenName': transfer['tokenName'],
                'tokenSymbol': transfer['tokenSymbol'],
                'decimals': int(transfer['tokenDecimal']),
                'amount': 0
            }
        tokens[contract]['amount'] += int(transfer['value'])
    return [{'contractAddress': k, **v} for k, v in tokens.items()]

def convert_wei_to_decimal(value, decimals):
    return int(value) / (10 ** decimals)