from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class RegisterUser(UserCreationForm):
    class meta:
       model = User
       fields = ["username","password1","password2"]

class ComfirmUser(forms.Form):
    username = forms.CharField()
    new_password = forms.CharField(widget=forms.PasswordInput,label="new password")
    confirm_password = forms.CharField(widget=forms.PasswordInput,label="confirm password")

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")
        if new_password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        
        try:
            validate_password(new_password)
        except ValidationError as e:
                self.add_error("new_password", e)
                
        return cleaned_data