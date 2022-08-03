# from tkinter import CASCADE
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


class Channel(models.Model):
	channel_name = models.CharField(max_length=200, null=True)
	strategy = models.ForeignKey(Strategy, null=True, on_delete=models.CASCADE)
	
	def __str__(self) -> str:
		return self.channel_name

class Country(models.Model):
	country_name = models.CharField(max_length=200, null=True)
	channel = models.ForeignKey(Channel, null=True, on_delete=models.CASCADE)

	def __str__(self) -> str:
		return self.country_name

class Ad(models.Model):
	ad_name = models.CharField(max_length=200, null=True)
	country = models.ForeignKey(Country, null=True, on_delete=models.CASCADE)

	def __str__(self) -> str:
		return self.ad_name
