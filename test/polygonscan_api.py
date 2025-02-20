import requests
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

API_URL = "https://api.polygonscan.com/api"
API_KEY = os.getenv('POLYGONSCAN_API_KEY')

def get_balance(address):
    response = requests.get(API_URL, params={
        'module': 'account',
        'action': 'balance',
        'tag': 'latest',
        'address': address,
        'apikey': API_KEY
    })
    data = response.json()

    if data['status'] == '1':
        return int(data['result'])
    else:
        raise Exception("Error fetching balance: " + data['message'])

def get_token_transfers(address):
    response = requests.get(API_URL, params={
        'module': 'account',
        'action': 'tokentx',
        'address': address,
        'apikey': API_KEY
    })
    if response.status_code == 200:
        return response.json().get('result', [])
    return []

def get_token_balances(address, contract_address):
    response = requests.get(API_URL, params={
        'module': 'account',
        'action': 'tokenbalance',
        'contractaddress': contract_address,
        'address': address,
        'apikey': API_KEY
    })
    if response.status_code == 200:
        return response.json().get('result', '0')
    return '0'