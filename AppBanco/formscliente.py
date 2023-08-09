from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=['Nombre','Apellido','Correo','Celular']

        widgets = {
            'Nombre':forms.TextInput(attrs={'placeholder':'Nombre'}),
            'Apellido':forms.TextInput(attrs={'placeholder':'Apellido'}),
            'Correo':forms.TextInput(attrs={'placeholder':'Correo'}),
            'Celular':forms.TextInput(attrs={'placeholder':'Celular'}),
        }