from django import forms
from webpage.models import TextFile


class TextFileForm(forms.ModelForm):
    class Meta:
        model = TextFile
        fields = ['name', 'file']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'имя файла...',
                                           'class': 'custom-form-control input-group mb-3 '}),
        }
        labels = {
            'name': 'Имя файла',
            'file': 'Загрузить файл',
        }

