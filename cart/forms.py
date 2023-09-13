from django import forms
from furnitures import models


class CartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, widget=forms.HiddenInput())
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
