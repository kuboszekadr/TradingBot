from abc import ABC, abstractmethod


class AbstractExchangeToSignal(ABC):
    """
    Basic class to inherit in order to implement stock market algorithms
    and return signal.
    """

    @abstractmethod
    def get_signal(self, exchange):
        """
        Return signal:
        0 -> sell
        1 -> do nothing
        2 -> buy
        """
        pass
