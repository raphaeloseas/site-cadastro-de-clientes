from multiprocessing.sharedctypes import Value
from socket import fromshare
from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    data_de_nascimento = forms.DateField(
        widget=forms.TextInput(
            attrs={"type": "date"}
        )
    )
    class Meta:
        model = Client
        fields = ('nome',
                  'logradouro',
                  'numero',
                  'bairro',
                  'cidade',
                  'estado',
                  'telefone',
                  'email',
                  'data_de_nascimento'
        )