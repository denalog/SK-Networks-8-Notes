from abc import ABC, abstractmethod


class ExcelBasicService(ABC):
    @abstractmethod
    def createExcelToDatabase(self):
        pass
