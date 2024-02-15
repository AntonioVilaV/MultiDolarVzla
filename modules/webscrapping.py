from abc import ABC, abstractmethod


class DolarSource(ABC):
    @abstractmethod
    def get_dolar_data(self):
        pass

    @abstractmethod
    def clean_data(self):
        pass

    @abstractmethod
    def get_dolar_price(self):
        pass
