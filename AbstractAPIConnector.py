import requests

from abc import ABC, abstractmethod

import logging
import requests


class AbstractAPIConnector(ABC):
    """
    Abstract class which should be used as base for all api connections.
    """
    __api_url = "https://api.zonda.exchange/rest/trading/"
    
    def get_response_for_market(self, api_path, market_code=''):
        """
        Connect with api and returns message per chosen market.
        If no market choosen, returns messages for all available markets (if possible).
        """
        code = '' if market_code == '' else '/' + market_code
        url = self.__api_url + api_path + code
        print(url)
        try:
            response = requests.get(url)
        except Exception as e:
            logging.exception(e.message)
            return
        if response.status_code == 200:
            return response.json()
        logging.warning(f"API call end with response code {response.status_code}.")
