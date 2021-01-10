import re

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

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if len(first_name) < 1:
            raise forms.ValidationError("Это обязательное поле")
        return first_name

    def clean_password2(self):
        pattern_password = re.compile(
            r"^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z$%#^]{8,}$"
        )
        password_re = pattern_password.match(self.cleaned_data["password2"])
        valid = self.cleaned_data["password1"] == self.cleaned_data["password2"]
        if not valid:
            raise forms.ValidationError("Пароли не совпадают")
        if not password_re:
            raise forms.ValidationError("Пароль не валиден")
        return self.cleaned_data["password2"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким E-mail уже существует")
        return email
