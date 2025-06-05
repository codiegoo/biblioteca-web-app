from django import forms
from .models import Usuario, Libro, Prestamo, Autor
from django.utils.safestring import mark_safe


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        exclude = ['disponible']

    def __init__(self, *args, **kwargs):
        super(LibroForm, self).__init__(*args, **kwargs)
        # No necesitas hacer nada más aquí


class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = '__all__'
        widgets = {
            'fecha_devolucion': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['libro'].queryset = Libro.objects.filter(disponible=True) | Libro.objects.filter(pk=self.instance.libro.pk)
        else:
            self.fields['libro'].queryset = Libro.objects.filter(disponible=True)




class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'
