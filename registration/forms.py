from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserForm(UserCreationForm):
    """ Форма регистрации нового пользователя """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)
        error_messages = {
            'username': {
                'unique_together': 'Пользователь с таким именем уже существует...',
                'unique': 'Пользователь с таким именем уже существует...'
            },
            'password2': {
                'password_mismatch': 'Пароли не совпадают!'
            }
        }


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