# checkwxapi
Python wrapper around the CheckWX api.

`This code is not production ready`

## Authentication
CheckWXAPI requires an API Key to make requests. You can obtain a key [here](https://www.checkwxapi.com/user/api) by creating an account.

## Installation
Install this package by running this command: `pip install checkwxapi`

## Using this package

```python
import asyncio
import logging

from checkwxapi import (
    CheckWXAPI
)
from aiohttp import ClientError, ClientSession

ICAO_CODE = "KSDF"
API_KEY = "xxxxx"

logging.basicConfig(level=logging.DEBUG)


async def main():
    async with ClientSession() as httpClient:
        try:
            checkwxapi = CheckWXAPI(
                API_KEY, httpClient
            )
            metar = await checkwxapi.async_get_metar(ICAO_CODE)
            taf = await checkwxapi.async_get_ftaf(ICAO_CODE)
        except (
            ApiError,
            InvalidApiKeyError
        ) as error:
            print(f"Error: {error}")
        else:
            print(f"Current: {metar}")
            print(f"Forecast: {taf}")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
```
