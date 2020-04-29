from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserForm(UserCreationForm):
    """ Форма регистрации нового пользователя """

    error_messages = {
        'password_mismatch': "Введены не совпадающие пароли"
    }

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)


class LoginForm(forms.Form):

    login = forms.CharField(
        required=True,
        widget=forms.TextInput(),
        max_length=64
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        max_length=64
    )