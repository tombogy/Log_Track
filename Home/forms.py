# driver/forms.py

from django import forms
from Driver.models import LogisticUser

class DriverForm(forms.ModelForm):
    class Meta:
        model = LogisticUser
        fields = ['name', 'mobile',  'email', 'password', 'liscence']
