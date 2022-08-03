from django.forms import ModelForm
from .models import Client, Phase, Strategy, Plan

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class PlanForm(ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'
        # exclude = ['client']

class PhaseForm(ModelForm):
    class Meta:
        model = Phase
        fields = '__all__'

class StrategyForm(ModelForm):
    class Meta:
        model = Strategy
        fields = '__all__'

