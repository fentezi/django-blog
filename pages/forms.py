from django import forms
from django.core.mail import send_mail


class EmailForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    message = forms.CharField(max_length=500)

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        return send_mail(
            name,
            message,
            email,
            ['serouhn@gmail.com'],
            fail_silently=False,
        )
