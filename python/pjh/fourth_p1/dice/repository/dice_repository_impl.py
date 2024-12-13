import random

from dice.entity.dice import Dice
from dice.repository.dice_repository import DiceRepository
from game.entity.game import Game


class DiceRepositoryImpl(DiceRepository):
    __instance = None

    # 빈 리스트를 생성하여 여기에 주사위 정보를 저장하려고 함
    # 즉 이번 케이스는 rollDice()가 구동 될 때마다 diceList에 내용이 누적됨
    # 빈 리스트를 생성하는 문법입니다.
    __diceList = []
    __skilldiceList = []

    MIN = 1
    MAX = 6

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def rollFirstDice(self):
        diceNumber = random.randint(self.MIN, self.MAX)
        dice = Dice(diceNumber)
        # append() 붙이기를 통해서
        # 생성자로 만든 dice를 __diceList에 추가하였습니다.
        self.__diceList.append(dice)

        return self.__diceList


    # 누적된 전체 리스트를 가져오게 됨
    def acquireDiceList(self):
        return self.__diceList

    def SkilldicePlayerList(self):
        playerList = Game.getGameMap()
        skilldicePlayer = playerList.values()
        if skilldicePlayer %2 == 0:
            return self.rollSkilldice()
        return None

    def rollSkilldice(self):
        diceNumber = random.randint(self.MIN, self.MAX)
        dice = Dice(diceNumber)
        self.__skilldiceList.append(dice)

