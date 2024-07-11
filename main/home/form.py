from django import forms

class person(forms.Form):
    first_name = forms.CharField(max_length=55)
    last_name = forms.CharField(max_length=55)