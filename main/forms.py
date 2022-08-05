from django import forms
from django.forms import ModelForm
from .models import Client, Phase, Strategy, Plan

class ClientForm(ModelForm):

    class Meta:
        model = Client
        fields = ['client_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client_name'].widget.attrs['autofocus'] = 'on'

class PlanForm(ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'
        exclude = ['client']

class PhaseForm(ModelForm):
    class Meta:
        model = Phase
        fields = '__all__'
        exclude = ['plan']

class StrategyForm(ModelForm):
    class Meta:
        model = Strategy
        fields = '__all__'
        exclude = ['phase']

