from django import forms
from .models import *


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'city', 'sub_city', 'home_number', 'phone_number']
