from django import forms
CHOICES=[(i , str(i)) for i in range(1,21)]

class ProductAddForm(forms.Form):
    quantity =forms.TypedChoiceField(choices=CHOICES ,coerce=object)
    override = forms.BooleanField(required=False , initial=False , widget=forms.HiddenInput)