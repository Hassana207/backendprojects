from .models import Booking
from django import  forms

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["name","email","barber","services","date"]
        widgets = {
            "services": forms.CheckboxSelectMultiple(),
            "date": forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }