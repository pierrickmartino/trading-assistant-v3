# Wallet Address Tracker Scope Document

## Introduction
This document outlines the scope for developing a Wallet Address Tracker that will search the Polygon network using the PolygonScan API. The tracker will identify different tokens held by a specified wallet address where the total quantity of each token is greater than 0.

## API Endpoints

### 1. Get Token Balance for an Address
- **Endpoint:** `https://api.polygonscan.com/api`
  
#### Usage and Query Parameters:
- **`module`**: Set to `account`
- **`action`**: Set to `tokenbalance`
- **`contractaddress`**: The contract address of the token (e.g. ERC-20 token).
- **`address`**: The wallet address you want to check.
- **`tag`**: (Optional) Defaults to "latest".
- **`apikey`**: Your valid API key for PolygonScan.

#### Example Request:
```
https://api.polygonscan.com/api?module=account&action=tokenbalance&contractaddress=0x...&address=0x...&tag=latest&apikey=YourAPIKey
```

#### Response JSON Format:
```json
{
  "status": "1",
  "message": "OK",
  "result": "1000000000000000000"  // Token balance in the smallest unit
}
```

### 2. Get All ERC-20 Token Transfers for an Address
- **Endpoint:** `https://api.polygonscan.com/api`
  
#### Usage and Query Parameters:
- **`module`**: Set to `account`
- **`action`**: Set to `tokentx`
- **`address`**: The wallet address you want to check.
- **`startblock`**: (Optional) Start block number. Defaults to 0.
- **`endblock`**: (Optional) End block number. Defaults to 99999999.
- **`sort`**: Sort direction (asc|desc).
- **`apikey`**: Your valid API key for PolygonScan.

#### Example Request:
```
https://api.polygonscan.com/api?module=account&action=tokentx&address=0x...&sort=asc&apikey=YourAPIKey
```

#### Response JSON Format:
```json
{
  "status": "1",
  "message": "OK",
  "result": [
    {
      "blockNumber": "12345678",
      "timeStamp": "1616749005",
      "hash": "0x...",
      "from": "0x...",
      "to": "0x...",
      "contractAddress": "0x...",
      "tokenName": "TokenName",
      "tokenSymbol": "TKN",
      "tokenDecimal": "18",
      "value": "1000000000000000000"
    }
    // More transactions
  ]
}
```

## Limitations of APIs
- Rate Limits: The free version of the PolygonScan API has strict rate limits (5 requests/sec), which can throttle performance when multiple checks are made in succession.
- Requires API Key: All requests need a valid API key, causing potential access issues if key is compromised or used up.
- Token Details: More specific token details (e.g., metadata, symbols) would require additional APIs or a more complex implementation where several contract addresses need to be checked.

## Optimization for Better Performance
- Batch Requests: If possible, batch multiple wallet addresses or token requests to reduce the number of API calls.
- Caching Results: Store the token balances locally for repeat checks, refreshing them after a certain time period to minimize calls.
- Asynchronous Calls: Use asynchronous programming (e.g. `asyncio` in Python) to avoid blocking whenever multiple requests are made.

## Asset Calculation and Aggregation
1. Upon retrieving the balances for each token, convert the result from the smallest unit to standard denomination based on the token's decimal placements defined in the ERC-20 contract.
2. Aggregate and count unique tokens with total quantities greater than zero.
3. Store results in a structured format (e.g., dictionary or list of tuples) for later processing and display.

## Possible Next Steps
1. Implement a user interface to input wallet addresses and display token results.
2. Add comprehensive error checks for API responses to handle failures gracefully.
3. Define additional features like real-time updates for asset values and historical transaction views.
4. Enhance functionality with reporting features for asset diversity and historical balance tracking.

## Relevant Documentation Pages
1. [PolygonScan API Documentation](https://docs.polygonscan.com/)
2. [Accounts API Endpoints](https://docs.polygonscan.com/api-endpoints/accounts)
3. [Tokens API Endpoints](https://docs.polygonscan.com/api-endpoints/tokens)
4. [Rate Limits Documentation](https://docs.polygonscan.com/support/rate-limits)
5. [PolygonScan API Usage Statistics](https://docs.polygonscan.com/getting-started/viewing-api-usage-statistics)

This scope document lays the groundwork for our Wallet Address Tracker project that will efficiently utilize the PolygonScan API while ensuring a good user experience.