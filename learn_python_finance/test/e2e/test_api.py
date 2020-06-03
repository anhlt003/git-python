import uuid
import datetime
import config
import decimal
import requests
import pytest

@pytest.mark.usefixtures('restart_api')
def test_unhappy_path_returns_400_and_error_message():
        orderdata =  {
            "order_id": "order_55", 
            "order_item": "E2E", 
            "order_start_time":"2020-05-26 14:53:47",
            "order_end_time": "2020-05-26 14:53:47",
            'order_price': 1000.00,
            "order_lot": 0.10,
            "order_margin": 1,
            "order_stoploss": 0.00,
            "order_takeprofit": 100.00}
        print(orderdata)
        url = config.get_api_url()
        r = requests.post(f'{url}/allocate', json=orderdata)
        assert r.status_code == 400
        assert r.json()['message'] == f'batchId is batch_55'