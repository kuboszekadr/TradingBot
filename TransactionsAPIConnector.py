from requests.models import Response
from AbstractAPIConnector import AbstractAPIConnector


class TransactionsAPIConnector(AbstractAPIConnector):
    __api_path = "transactions"

    def get_transactions_exchange(self, market_code=''):
        response_json =  super().get_response_for_market(self.__api_path, market_code)
        exchange = [item['r'] for item in response_json['items']]
        return exchange


if __name__ == "__main__":
    xx = TransactionsAPIConnector()
    xx.get_transactions_exchange("DAI-PLN")
