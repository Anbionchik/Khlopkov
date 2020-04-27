from django import forms
from main.models import ListModel


class ListForm(forms.ModelForm):
    """
    Форма надстроек расписания обмена
    """
    name = forms.CharField(widget=forms.TextInput())
    user = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = ListModel
        fields = ('name', 'user')
