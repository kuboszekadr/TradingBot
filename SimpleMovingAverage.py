from AbstractExchangeToSignal import AbstractExchangeToSignal


class SimpleMovingAverage(AbstractExchangeToSignal):
    """
    Use simple moving average to calculate signals and make decision
    to buy, sell or do nothing on stock market.
    """

    def __init__(self, samples_amount: int=2):
        # calculating average to make sens requires one sample
        # need to calculate two moving averages and API returns 10 samples,
        # so cannot have more than 9 samples in one moving average
        self.samples_amount = min(max(1, samples_amount), 9)

    def get_signal(self, exchanges):
        """
        Implement simple moving average and return signal:
        0 -> sell
        1 -> do nothing
        2 -> buy
        """
        # first moving average
        fma = sum(exchanges[len(exchanges)-self.samples_amount-1:-1]) / self.samples_amount
        # second moving average
        sma = sum(exchanges[len(exchanges)-self.samples_amount:]) / self.samples_amount
        # one before last exchange
        prev_exchange = exchanges[-2]
        # last exchange
        last_exchange = exchanges[-1]

        if sma - fma >= 0 and last_exchange - prev_exchange >= 0:
            return 2
        if sma - fma <= 0 and last_exchange - prev_exchange < 0:
            return 0
        return 1