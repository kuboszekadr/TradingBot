from market.AbstractAPIConnector import AbstractAPIConnector


class TransactionsAPIConnector(AbstractAPIConnector):  #TODO change for composition
    _api_path = "transactions"

    def get_transactions_exchange(self, market_code=''):
        response_json =  super().get_response_for_market(self._api_path, market_code)
        exchange = [item['r'] for item in response_json['items']]
        return exchange


if __name__ == "__main__":
    conn = TransactionsAPIConnector()
    conn.get_transactions_exchange("DAI-PLN")
