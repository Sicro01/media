from sqlite3 import Date
from django import forms
from django.forms import ModelForm
from .models import Client, Plan, Phase, Strategy, Country, Channel, Ad, TargetCountry, TargetChannel

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

class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['country_name'].widget.attrs['autofocus'] = 'on'

class ChannelForm(ModelForm):
    class Meta:
        model = Channel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['channel_name'].widget.attrs['autofocus'] = 'on'

class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ad_name'].widget.attrs['autofocus'] = 'on'

class TargetCountryForm(ModelForm):
    class Meta:
        model = TargetCountry
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['strategy_name'].widget.attrs['autofocus'] = 'on'

class TargetChannelForm(ModelForm):
    class Meta:
        model = TargetChannel
        fields = '__all__'