from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class CreationUserForm(UserCreationForm):
    date_of_birth = forms.DateField(
        label=("Дата рождения"),
        widget=forms.TextInput(attrs={"type": "date"}),
    )
    password1 = forms.CharField(label=("Пароль"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=("Повторите пароль"), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "date_of_birth",
            "email",
            "photo",
        ]
