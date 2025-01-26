# import libraries
import numpy as np
import requests
from datetime import datetime
from requests.exceptions import HTTPError


# class to request calls from api
# https://random-data-api.com/api/
class Requests(object):

    # create artificial [user_id]
    # set 10.000 users [only]
    @staticmethod
    def gen_user_id(size):
        return np.random.randint(1, 10000, size=size)

    # current timestamp
    # set date and time
    @staticmethod
    def gen_timestamp():
        return datetime.now()

    # get requests method
    @staticmethod
    def api_get_request(url, params):
        try:
            dt_request = requests.get(url=url, params=params)
            dt_request.raise_for_status()
            dict_request = dt_request.json()
            return dict_request
        except HTTPError as http_err:
            print(f"http error occurred: {http_err}")
        except Exception as err:
            print(f"api not available at this moment.: {err}")
        return {}
