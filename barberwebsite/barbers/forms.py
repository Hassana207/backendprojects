from django import forms
from .models import BarberInfo

class SetBarberInfo(forms.ModelForm):
    class Meta:
        model = BarberInfo
        fields = ["name","bio","skills","photo","email","number","services"]

        widgets = {
            "services": forms.CheckboxSelectMultiple(),
        }

class RateBarberService(forms.ModelForm):
    class Meta:
        model = BarberInfo
        fields = ["reviews"]
