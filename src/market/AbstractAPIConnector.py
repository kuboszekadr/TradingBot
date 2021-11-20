from abc import ABC, abstractmethod


class AbstractMarket(ABC):
    """
    Abstract class which should be used as base for all api connections.
    """
    _api_url = "https://api.zonda.exchange/rest/trading/"  # TODO

    @abstractmethod
    def get_response_for_market(self, api_path, market_code=''):
        """
        Connect with api and returns message per chosen market.
        If no market choosen, returns messages for all available markets (if possible).
        """
        pass