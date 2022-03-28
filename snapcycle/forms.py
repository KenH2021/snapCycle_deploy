from django import forms


class EmailForm(forms.Form):
    email_address = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'placeholder': 'Adresse Courriel', 'style': 'width: 90vh;height:75px;', 'class': 'form-control form-control-lg'}))
