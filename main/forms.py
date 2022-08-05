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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client'].widget.attrs['autofocus'] = 'on'

class PhaseForm(ModelForm):
    class Meta:
        model = Phase
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['plan'].widget.attrs['autofocus'] = 'on'
        self.fields['phase_start_date'].widget.attrs['data-provide'] = 'datepicker'
        self.fields['phase_end_date'].widget.attrs['data-provide'] = 'datepicker'

class StrategyForm(ModelForm):
    class Meta:
        model = Strategy
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phase'].widget.attrs['autofocus'] = 'on'
        self.fields['strategy_start_date'].widget.attrs['data-provide'] = 'datepicker'
        self.fields['strategy_end_date'].widget.attrs['data-provide'] = 'datepicker'

