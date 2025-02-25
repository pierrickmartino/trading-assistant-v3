import requests

class PolygonscanAPI:
    BASE_URL = "https://api.polygonscan.com/api"

    def __init__(self, api_key):
        self.api_key = api_key

    def _make_request(self, module, action, **kwargs):
        params = {
            "module": module,
            "action": action,
            "apikey": self.api_key
        }
        params.update(kwargs)
        response = requests.get(self.BASE_URL, params=params)
        if response.status_code != 200:
            raise Exception(f"API call failed with status {response.status_code}")

        result = response.json()
        if 'status' in result and result['status'] != '1':
            raise Exception(result['result'])
        return result

    def get_token_transactions(self, address):
        params = {
            "module": "account",
            "action": "tokentx",
            "address": address,
            "startblock": 0,
            "endblock": 99999999,
            "sort": "asc"
        }
        return self._make_request(**params)