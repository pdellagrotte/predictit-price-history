from urllib.request import urlopen
import json
import sqlite3
import os


url_root = "https://www.predictit.org/api/Public/GetMarketChartData/"
# https://www.predictit.org/api/Public/GetMarketChartData/5136?timespan=24h&maxContracts=6&showHidden=true

all_contracts_url = 'https://www.predictit.org/api/marketdata/all/'

# contract_id = "3352"
# time_interval = "90d"  #24h, 7d, 30d, 90d

# url = url_root + contract_id + "?timespan" + time_days + "&maxContracts=6&showHidden=true"

# print(url)

def build_url(contract_id, time_interval, max_contracts="6", show_hidden="true"):
    url_root = "https://www.predictit.org/api/Public/GetMarketChartData/"
    url = url_root + contract_id + "?timespan=" + time_interval + "&maxContracts=" + max_contracts
    url = url + "&showHidden=" + show_hidden
    print(url)
    return url


def get_json_data(url: str):
    response = urlopen(url)
    xml = response.read().decode('utf-8')
    json_response = json.loads(xml)
    return json_response


def get_list_of_markets():
    response = urlopen(all_contracts_url)
    xml = response.read().decode('utf-8')
    json_response = json.loads(xml)
    market_list = []
    for market in json_response['markets']:
        market_list.append(market['id'])
    return market_list
