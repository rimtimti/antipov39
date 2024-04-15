from django import forms
from django.forms import TextInput
from main.models import Query, NumberHistory


class NumberForm(forms.ModelForm):
    class Meta:
        model = NumberHistory
        fields = ["cadastral_number"]
        widgets = {
            "cadastral_number": TextInput(
                attrs={"style": "width: 100%", "placeholder": "XX:XX:XXXXXX:XXX"}
            ),
        }


class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ["cadastral_number", "latitude", "longitude"]
        widgets = {
            "cadastral_number": TextInput(
                attrs={"style": "width: 100%", "placeholder": "XX:XX:XXXXXX:XXX"}
            ),
            "latitude": TextInput(
                attrs={"style": "width: 100%", "placeholder": "XX.XX"}
            ),
            "longitude": TextInput(
                attrs={"style": "width: 100%", "placeholder": "XX.XX"}
            ),
        }
