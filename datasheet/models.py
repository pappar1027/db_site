from django.db import models
from django.utils import timezone

# Create your models here.
class Option(models.Model):
	contract_name=models.CharField(max_length=120)
	last_trade_date=models.DateTimeField('last trade date')
	strike=models.DecimalField(max_digits=20,decimal_places=2)
	last_price=models.DecimalField(max_digits=20,decimal_places=2)
	bid=models.DecimalField(max_digits=20,decimal_places=2)
	ask=models.DecimalField(max_digits=20,decimal_places=2)
	change=models.DecimalField(max_digits=20,decimal_places=2)
	percentage_change=models.CharField(max_length=120)
	volume=models.IntegerField()
	open_interest=models.IntegerField()
	implied_volatility=models.CharField(max_length=120)
	last_edit=models.DateTimeField('last edit date',default=timezone.now())

