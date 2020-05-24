from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import Profile, User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "email",
            "username",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "email",
            "username",
        )


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio", "location", "profile_pic")
