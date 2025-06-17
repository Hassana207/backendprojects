from django import forms
from . models import Service


class ServiceForm(forms.ModelForm):
    class meta:
        model = Service
        fields = ["name","price"]