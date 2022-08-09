# from tkinter import CASCADE
from tkinter import Widget
from django.db import models
import datetime

class Client(models.Model):
	client_name = models.CharField(max_length=200, null=True)

	def __str__(self) -> str:
		return self.client_name

class Plan(models.Model):
	plan_name = models.CharField(max_length=200, null=True)
	client = models.ForeignKey(Client, null=True, on_delete=models.CASCADE)

	def __str__(self) -> str:
		return self.plan_name

class Phase(models.Model):
	phase_name = models.CharField(max_length=200, null=True)
	phase_start_date = models.DateField(default=datetime.date.today)
	phase_end_date = models.DateField(default=datetime.date.today)
	plan = models.ForeignKey(Plan, null=True, on_delete=models.CASCADE)
	
	def __str__(self) -> str:
		return self.phase_name

class Strategy(models.Model):
	strategy_name = models.CharField(max_length=200, null=True)
	strategy_start_date = models.DateField(default=datetime.date.today)
	strategy_end_date = models.DateField(default=datetime.date.today)
	phase = models.ForeignKey(Phase, null=True, on_delete=models.CASCADE)

	def __str__(self) -> str:
		return self.strategy_name

class Country(models.Model):
	country_name = models.CharField(max_length=200, null=True)
	targetcountries = models.ManyToManyField(Strategy, through='TargetCountry')

	def __str__(self) -> str:
		return self.country_name

class TargetCountry(models.Model):
	strategy = models.ForeignKey(Strategy, null=True, on_delete=models.CASCADE)
	country = models.ForeignKey(Country, null=True, on_delete=models.CASCADE)
	
	def __str__(self) -> str:
		return (f'{self.strategy}:{self.country}')

class Channel(models.Model):
	channel_name = models.CharField(max_length=200, null=True)
	targetchannels = models.ManyToManyField(TargetCountry, through='TargetChannel')
	
	def __str__(self) -> str:
		return self.channel_name

class TargetChannel(models.Model):
	targetcountry = models.ForeignKey(TargetCountry, null=True, on_delete=models.CASCADE)
	channel = models.ForeignKey(Channel, null=True, on_delete=models.CASCADE)

	def __str__(self) -> str:
		return (f'{self.targetcountry}:{self.channel}')

class Ad(models.Model):
	ad_name = models.CharField(max_length=200, null=True)

	def __str__(self) -> str:
		return self.ad_name

class ChannelAd(models.Model):
	channel = models.ForeignKey(Channel, null=True, on_delete=models.CASCADE)
	ad = models.ForeignKey(Ad, null=True, on_delete=models.CASCADE)
	
	def __str__(self) -> str:
		return (f'{self.channel}:{self.ad}')
