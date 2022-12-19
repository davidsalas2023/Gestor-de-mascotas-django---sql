from django import forms
from mascotaplus.models import Mascotas



class FormMascotas(forms.ModelForm):
        class Meta:

            model= Mascotas
            fields= '__all__'
            widget= {
            'mas': forms.widgets.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.widgets.TextInput(attrs={'class':'form-control'}),
            'especie': forms.widgets.Select(attrs={'class':'form-control'})

    }
