import sys
import json
from datetime import datetime
from requests import Session

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '4a9bbdcd-79ea-4420-b4e4-c177fa51227e',
}
session = Session()
session.headers.update(headers)


def test_access_to_10_tickers_sorted_by_volume():
    parameters = {
        'sort': 'volume_24h',
        'limit': '10',
    }
    time_before_response = datetime.now().microsecond
    response = session.get(url, params=parameters)
    time_after_response = datetime.now().microsecond
    data = json.loads(response.text)

    assert time_after_response - time_before_response < 500000, "Response time is more than 500 ms"
    assert str(datetime.utcnow().date()) in data['status']['timestamp'], "Date is out of scope"
    assert sys.getsizeof(data) < 10000, "Response size is more than 10 Kbyte"
