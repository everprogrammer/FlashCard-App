from django import forms

class CardCheckForm(forms.Form):
    card_id = forms.IntegerField(required=True)
    solved = forms.CharField(required=False)