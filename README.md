# My Crypto Prices

## Overview
This project retrieves historical cryptocurrency prices from CryptoCompare and stores them in a TimeScaleDB instance. 
The application uses [PydanticAI](https://ai.pydantic.dev/) to create an Agent that coordinates the logic:
1. Checks if a daily price is already stored in the DB.
2. If not, queries the CryptoCompare API for that day’s price.
3. Stores/retrieves the data from TimeScaleDB.

## Tech Stack
- Python 3.11
- [TimeScaleDB](https://www.timescale.com/)
- [CryptoCompare API](https://min-api.cryptocompare.com/documentation)
- [PydanticAI](https://ai.pydantic.dev/) for Agent interface
- Docker & Docker Compose

## Quick Start
Steps to be filled in after we finalize the Docker setup.

## License
To be decided by you or your organization.
