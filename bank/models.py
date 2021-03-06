from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    SAVINGS = 'SV'
    CHECKING = 'CH'
    MONEY_MARKET = 'MM'
    CD = 'CD'
    IRA_CD = 'IC'
    PRODUCT_CHOICES = [
        (SAVINGS, 'Savings'),
        (CHECKING, 'Checking'),
        (MONEY_MARKET, 'Money Market'),
        (CD, 'CD'),
        (IRA_CD, 'IRA CD'),
    ]

    product_type = models.CharField(
        max_length = 2,
        choices=PRODUCT_CHOICES
    )
    money = models.DecimalField(max_digits=19, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}: {self.product_type} - {self.money}'

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to=f'documents')

    def __str__(self):
        return f'{self.user.username}: {self.file}'