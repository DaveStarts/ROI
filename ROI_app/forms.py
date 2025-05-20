from django import forms
from .models import Programm

class ProgrammForm(forms.ModelForm):
    class Meta:
        model = Programm
        fields = ['name']
        labels = {'name': 'Programmname'}
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name des Programms eingeben'}),
        }