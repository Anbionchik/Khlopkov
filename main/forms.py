from django import forms
from main.models import ListModel


class ListForm(forms.ModelForm):
    """
    Форма надстроек расписания обмена
    """
    name = forms.CharField(required=True, widget=forms.TextInput())

    class Meta:
        model = ListModel
        fields = ('name', 'user')