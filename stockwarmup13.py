#!/usr/bin/python3

import requests
import json
import datetime

from pprint import pprint as print
def main():
    mylookup = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=2KTFTC2EFAYWX0MV'
    stockdata = requests.get(mylookup)
    json_data = stockdata.json()

    lastrefresh = json_data['Meta Data']['3. Last Refreshed']

    print(json_data['Time Series (5min)'][lastrefresh])


main()


