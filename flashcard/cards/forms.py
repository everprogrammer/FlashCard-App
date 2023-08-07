from django import forms

class CardCheckForm(forms.Form):
    card_id = forms.IntegerField(widget=forms.HiddenInput())
    solved = forms.BooleanField(required=False)