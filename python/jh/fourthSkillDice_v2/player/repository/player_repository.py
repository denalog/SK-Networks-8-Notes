from abc import ABC, abstractmethod

class PlayerRepository(ABC):

    @abstractmethod
    def createName(self):
        pass

    @abstractmethod
    def findByPlayerId(self, playerId):
        pass