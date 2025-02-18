from stock.repository.stock_repository import StockRepository


class StockRepositoryImpl(StockRepository):
    __instance = None

    __billList = []

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def asdf(self):
        print()


