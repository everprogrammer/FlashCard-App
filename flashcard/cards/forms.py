from django import forms

class CardCheckForm(forms.Form):
    card_id = forms.IntegerField(required=True)
    # Due to discrepancy in front-end, used CharField instead of BooleanField
    solved = forms.CharField(required=False)
    