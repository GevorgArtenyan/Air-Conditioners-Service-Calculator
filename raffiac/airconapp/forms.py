from django import forms

class AirConCalc(forms.Form):
    title = forms.CharField(max_length=100)
    your_name = forms.CharField(max_length=100)



