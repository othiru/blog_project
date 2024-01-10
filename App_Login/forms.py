from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class signUpForm(UserCreationForm):
    email = forms.EmailField(label="Email Address", required=True)
    password2 = forms.CharField(label="Confirm Password ", required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class userProfileChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password")