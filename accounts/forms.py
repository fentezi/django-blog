from django.contrib.auth.forms import UserCreationForm
from . import models
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = models.SignUpModel
        fields = (
            'username',
            'email',
        )


