from django.contrib.auth.forms import UserCreationForm

from . import models


class SignUpForm(UserCreationForm):
    class Meta:
        model = models.SignUpModel
        fields = (
            'username',
            'email',
        )
