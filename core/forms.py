from django import forms
from .models import PrestacionMedica

class PrestacionMedicaForm(forms.ModelForm):
    class Meta:
        model = PrestacionMedica
        fields = ['codigo', 'titulo', 'especialidad', 'descripcion', 'arancel_base', 'duracion_minutos', 'estado', 'imagen', 'vigente']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: CARD-03'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidad': forms.Select(attrs={'class': 'form-select'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'arancel_base': forms.NumberInput(attrs={'class': 'form-control'}),
            'duracion_minutos': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'vigente': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_arancel_base(self):
        arancel = self.cleaned_data.get('arancel_base')
        if arancel is not None and arancel < 0:
            raise forms.ValidationError("El arancel base no puede ser un valor negativo.")
        return arancel