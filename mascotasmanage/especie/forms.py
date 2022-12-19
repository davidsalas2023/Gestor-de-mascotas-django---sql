from django import forms
from especie.models import Especie

class FormEspecie(forms.ModelForm):
    class Meta:
        model= Especie
        fields='__all__'
        widget={
        'es': forms.widgets.TextInput(attrs={'class':'form-control'}),
        'NombreEspecie': forms.widgets.NumberInput(attrs={'class':'form-control'})
        }