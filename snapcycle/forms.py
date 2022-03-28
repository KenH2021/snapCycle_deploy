from django import forms

class EmailForm(forms.Form):
    email = forms.CharField(label='Adresse Courriel', max_length=100 )