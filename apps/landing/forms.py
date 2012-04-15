
from django import forms

from django.utils.translation import ugettext as _

from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        
        if User.objects.filter(username=username).count() is not 0:
            raise forms.ValidationError(_("This username is not available."))

        return username

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
