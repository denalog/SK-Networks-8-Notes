from django.db import models

from account.entity.account import Account
from game_software.entity.game_software import GameSoftware


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="carts")
    gameSoftware = models.ForeignKey(GameSoftware, on_delete=models.CASCADE, related_name="carts")
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'cart'
        app_label = 'cart'

    def __str__(self):
        return f"Cart(id={self.id}, account={self.account}, gameSoftware={self.gameSoftware})"

    def getId(self):
        return self.id

    def getAccount(self):
        return self.account

    def getGameSoftware(self):
        return self.gameSoftware