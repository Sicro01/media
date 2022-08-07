from sqlite3 import Date
from django import forms
from django.forms import ModelForm
from .models import Client, Phase, Strategy, Plan
from bootstrap_datepicker_plus.widgets import DatePickerInput

class DateInput(forms.DateInput):
    input_type = 'date'

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
        widgets = {
                'phase_start_date': DateInput(),
                'phase_end_date': DateInput()
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['plan'].widget.attrs['autofocus'] = 'on'
        
class StrategyForm(ModelForm):
    class Meta:
        model = Strategy
        fields = '__all__'
        widgets = {
                'strategy_start_date': DateInput(),
                'strategy_end_date': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phase'].widget.attrs['autofocus'] = 'on'
        self.fields['strategy_start_date'].widget.attrs['data-provide'] = 'datepicker'
        self.fields['strategy_end_date'].widget.attrs['data-provide'] = 'datepicker'

