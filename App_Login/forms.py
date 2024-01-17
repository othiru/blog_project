from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.urls import reverse
from App_Login.models import userProfile


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].help_text = (
            "Raw passwords are not stored, so there is no way to see this user's password, "
            "but you can change the password using <a href='{}'>this form</a>."
        ).format(reverse("App_Login:passwordChange"))


class userPasswordChangeForm(PasswordChangeForm):
    new_password2 = forms.CharField(label="Confirm Password ", required=True, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ("old_password", "new_password1", "new_password2")


class userProfilePictureChangeForm(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = ("profile_pic",)