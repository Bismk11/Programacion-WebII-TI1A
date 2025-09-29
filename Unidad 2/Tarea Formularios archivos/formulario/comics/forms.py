from django import forms
from .models import Comic

class ComicForm(forms.ModelForm):
    class Meta:
        model = Comic
        fields = ['titulo', 'autor', 'editorial', 'archivo']
        labels = {
            'titulo': 'Título',
            'autor': 'Autor',
            'editorial': 'Editorial',
            'archivo': 'Archivo (PDF o Imagen)',
        }

    def clean_archivo(self):
        archivo_subido = self.cleaned_data.get('archivo')
        if archivo_subido:
            if archivo_subido.content_type not in ['application/pdf', 'image/jpeg', 'image/png']:
                raise forms.ValidationError("El archivo debe ser una imagen (JPEG, PNG) o un PDF.")
        return archivo_subido
