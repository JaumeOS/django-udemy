from django import forms
from .models import Persona

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = (
            'first_name',
            'surnames',
        )
    
    def clean_surnames(self):
        surnames = self.cleaned_data('surnames')
        if "a" in surnames:
            raise forms.ValidationError("El apellido no puede contener una \"a\"")