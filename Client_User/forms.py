from django.contrib.auth.forms import UserCreationForm
from django import forms
from Operation_User.models import USER


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = USER
        fields = ["email","password1", "password2"]

   