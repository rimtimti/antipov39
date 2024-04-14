from django import forms
from django.forms import TextInput
from main.models import Query, NumberHistory


class NumberForm(forms.ModelForm):
    class Meta:
        model = NumberHistory
        fields = ["cadastral_number"]
        widgets = {
            "cadastral_number": TextInput(attrs={"style": "width: 100%"}),
        }


class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ["cadastral_number", "latitude", "longitude"]
        widgets = {
            "cadastral_number": TextInput(attrs={"style": "width: 100%"}),
            "latitude": TextInput(attrs={"style": "width: 100%"}),
            "longitude": TextInput(attrs={"style": "width: 100%"}),
        }
